---
date: 2026-08-20
categories:
  - Tutorials
  - Agents
---

# Building a multi-agent system with LangGraph

A single agent with a big prompt and a pile of tools works fine until the task branches: one
part needs research, another needs code execution, another needs a human sign-off before it
does anything destructive. At that point you're better off with several narrow agents
coordinated by explicit control flow than one agent trying to hold all of it in its head.
LangGraph is built for exactly that — it models an agent system as a graph of nodes and edges
over a shared state, instead of a single hidden loop.

<!-- more -->

## Why a graph instead of a loop

The default "agent" pattern — LLM decides, calls a tool, sees the result, decides again — is
just a `while` loop with an implicit state machine buried inside the prompt. That's fine for a
single agent. It falls apart once you need:

- **Multiple specialised agents** (a researcher, a coder, a reviewer) that hand off to each
  other.
- **Conditional routing** — different paths depending on what happened earlier, not just what
  the LLM feels like doing next.
- **Human-in-the-loop checkpoints** before an irreversible action.
- **Retries and fallbacks** that are part of the architecture, not an afterthought wrapped in
  `try/except`.

LangGraph makes the control flow a first-class, inspectable graph instead of prompt-encoded
behaviour. That's the whole value proposition.

## Core concepts

Three things make up a LangGraph app:

1. **State** — a typed object (usually a `TypedDict` or Pydantic model) that flows through the
   graph. Every node reads from it and returns updates to it.
2. **Nodes** — plain Python functions (or agents) that take the state and return a partial
   update.
3. **Edges** — the wiring between nodes, either fixed or conditional (a function that inspects
   the state and decides where to go next).

```python
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    task: str
    plan: str
    research_notes: Annotated[list[str], operator.add]
    code: str
    review: str
    status: str
```

`Annotated[list[str], operator.add]` tells LangGraph how to merge updates when more than one
node writes to the same key — here, append rather than overwrite. Getting this reducer right is
the difference between agents silently clobbering each other's output and a state that
accumulates correctly.

## A supervisor + worker pattern

The pattern that scales best in practice is a **supervisor** node that decides which worker
runs next, rather than workers deciding among themselves.

```python
from langgraph.graph import StateGraph, END

def supervisor(state: AgentState) -> dict:
    if not state.get("plan"):
        return {"status": "planning"}
    if not state.get("research_notes"):
        return {"status": "researching"}
    if not state.get("code"):
        return {"status": "coding"}
    if not state.get("review"):
        return {"status": "reviewing"}
    return {"status": "done"}

def route(state: AgentState) -> str:
    return state["status"]

graph = StateGraph(AgentState)
graph.add_node("supervisor", supervisor)
graph.add_node("planner", planner_agent)
graph.add_node("researcher", researcher_agent)
graph.add_node("coder", coder_agent)
graph.add_node("reviewer", reviewer_agent)

graph.set_entry_point("supervisor")
graph.add_conditional_edges(
    "supervisor",
    route,
    {
        "planning": "planner",
        "researching": "researcher",
        "coding": "coder",
        "reviewing": "reviewer",
        "done": END,
    },
)

# each worker reports back to the supervisor, which decides what's next
for worker in ("planner", "researcher", "coder", "reviewer"):
    graph.add_edge(worker, "supervisor")

app = graph.compile()
```

Each `*_agent` function is an ordinary node: it takes `AgentState`, does its job (usually an LLM
call with a narrow, role-specific prompt and its own tool set), and returns the fields it's
responsible for. The supervisor never does the work itself — it only decides what runs next,
which keeps the routing logic testable independently of the agents' behaviour.

## Giving a worker its own tools

Each worker is free to be a full tool-calling agent internally — LangGraph doesn't care what's
inside a node, only what it returns.

```python
from langchain_core.tools import tool

@tool
def run_python(code: str) -> str:
    """Execute Python code in a sandbox and return stdout."""
    return sandbox.run(code)

def coder_agent(state: AgentState) -> dict:
    llm_with_tools = llm.bind_tools([run_python])
    response = llm_with_tools.invoke(
        f"Plan: {state['plan']}\nNotes: {state['research_notes']}\nWrite and test the code."
    )
    return {"code": response.content}
```

Keep each worker's tool set narrow and specific to its job. A researcher agent with access to
`run_python` and a coder agent with access to a search tool is how you end up with agents doing
each other's jobs badly instead of their own job well.

## Human-in-the-loop

For anything with real-world side effects — sending an email, deploying code, spending money —
add an explicit interrupt before the action node, rather than trusting the LLM to ask
permission on its own:

```python
app = graph.compile(interrupt_before=["coder"])
```

The graph pauses before `coder` runs; your application layer surfaces the pending state to a
human, and only resumes the graph on approval. This is a structural guarantee, not a prompt
instruction — it can't be talked out of it.

## Memory and checkpointing

LangGraph's checkpointer persists state after every node, which gives you two things for free:
resuming a long-running graph after a crash, and multi-turn conversations where state carries
over between calls.

```python
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string("checkpoints.db")
app = graph.compile(checkpointer=checkpointer)

app.invoke({"task": "..."}, config={"configurable": {"thread_id": "session-1"}})
```

Anything you'd otherwise hand-roll as "save state to a database after each step" is this, built
in.

## Where it breaks in production

- **Unbounded loops.** A supervisor that can route back to the same worker indefinitely needs an
  explicit step or retry counter in the state, or a bad LLM decision becomes an infinite loop
  and a very large bill.
- **State bloat.** `research_notes` accumulating across a long run eventually blows the context
  window of every downstream node. Summarise or truncate before it's handed to the next agent,
  don't just keep appending.
- **Silent partial failures.** A worker that throws should update `status` to something the
  supervisor can route on (`"failed"` → a recovery node), not just propagate an exception up
  through `.invoke()`.

## The shape of it

Plan the state schema first, the routing logic second, and the individual agent prompts last.
Most multi-agent systems that go wrong do so because the state design was an afterthought bolted
onto agents that were built first — get the shared state right and the graph wiring is
comparatively easy.
