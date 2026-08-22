---
date: 2026-08-22
categories:
  - Tutorials
  - RAG
---

# Building a RAG system from scratch

Retrieval-Augmented Generation (RAG) is the pattern you reach for when an LLM needs to answer
questions using knowledge it wasn't trained on — your docs, your codebase, your support
tickets. Instead of fine-tuning, you retrieve relevant context at query time and hand it to the
model. This is a practical walkthrough of the pieces that make a RAG system actually work in
production, not just in a notebook.

<!-- more -->

## The core idea

A RAG pipeline has two phases:

1. **Indexing** — chunk your documents, embed them, and store the vectors.
2. **Querying** — embed the user's question, retrieve the closest chunks, and feed them to the
   LLM as context alongside the question.

That's the whole idea. Everything below is about making each step hold up under real data and
real traffic.

## 1. Chunking

Bad chunking is the single most common reason a RAG system underperforms. A few rules that hold
up in practice:

- **Chunk by structure, not by character count.** Split on headings, paragraphs, or code blocks
  before falling back to a fixed size. A 500-token chunk that cuts a table in half is worse than
  a 700-token chunk that keeps it intact.
- **Overlap chunks by 10–20%.** This prevents an answer from being split across a chunk boundary
  where neither chunk has the full context.
- **Keep metadata with the chunk** — source file, section title, page number. You'll need it for
  citations and for filtering at query time.

```python
def chunk_document(text: str, chunk_size: int = 500, overlap: int = 75) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks
```

In practice, use a structure-aware splitter (e.g. one that respects Markdown headings or code
fences) rather than a naive sliding window — the snippet above is the baseline to understand,
not what you should ship.

## 2. Embeddings

Pick an embedding model based on your domain, not the leaderboard. A general-purpose model
(`text-embedding-3-small`, `bge-base`, etc.) is a fine default. If your corpus is heavily
technical or in a low-resource language, a domain- or language-tuned embedding model will
outperform a bigger general one — this is exactly the gap I've seen in Bangla NLP work, where
general multilingual embeddings miss nuance that a language-specific model catches.

Embed in batches, and cache the embeddings against a content hash so re-indexing doesn't mean
re-embedding everything.

## 3. Storage and retrieval

A vector database (PostgreSQL + `pgvector`, Qdrant, or similar) gives you approximate nearest
neighbour search over your chunk embeddings. Two things matter more than the choice of database:

- **Hybrid search.** Pure vector similarity misses exact matches — product codes, error
  messages, acronyms. Combine vector search with keyword (BM25) search and merge the results.
  This alone fixes a large share of "the answer was right there and it still missed it" bugs.
- **Re-ranking.** Retrieve more candidates than you need (say, top 20) with a cheap first pass,
  then re-rank with a cross-encoder to pick the top 3–5 that actually go into the prompt.
  Re-ranking is cheap relative to the LLM call and consistently improves answer quality.

## 4. Prompting the LLM

Once you have your retrieved chunks:

- Put the retrieved context **before** the question, clearly delimited.
- Tell the model explicitly to say when the context doesn't contain the answer, instead of
  guessing. This single instruction removes a large share of hallucinated answers.
- Include source references in the context so the model can cite them, and surface those
  citations in the response.

```text
Answer the question using only the context below. If the context doesn't contain the
answer, say so — do not guess.

Context:
{retrieved_chunks}

Question: {user_question}
```

## 5. Evaluation

You can't improve what you don't measure. At minimum, track:

- **Retrieval recall** — did the right chunk make it into the top-k?
- **Answer faithfulness** — is the answer actually supported by the retrieved context?
- **Latency** — embedding + retrieval + re-ranking + generation, end to end.

A small hand-labelled set of 30–50 question/answer pairs from your actual domain will tell you
more than any generic RAG benchmark.

## Where it breaks in production

The gap between a RAG demo and a RAG system that survives real traffic is usually one of:
stale indexes (documents change, embeddings don't get refreshed), unbounded context growth
(too many chunks stuffed into the prompt), or no fallback when retrieval returns nothing
relevant. Design for all three from day one rather than patching them in later.

That's the shape of it. The individual pieces — chunking, embeddings, hybrid search,
re-ranking, faithful prompting — are each simple on their own; the system is in how carefully
you wire them together.
