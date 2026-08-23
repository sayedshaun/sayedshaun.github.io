<div class="hero" markdown>
<img class="hero-photo" src="images/profile.jpg" alt="Sayed Shaun">
<div class="hero-body" markdown>

# Sayed Shaun

AI / ML Engineer · Dhaka, Bangladesh
{ .hero-role }

I build production AI systems — **LLM**, **agentic AI**, and the retrieval and
serving infrastructure around them. Currently at Synesis IT PLC, and preparing for a master's.

Open to roles & collaborations
{ .status }

</div>
</div>

<div class="tags" markdown>
<span>LLM</span>
<span>Agentic AI</span>
<span>RAG & retrieval</span>
<span>MLOps</span>
<span>Applied NLP</span>
</div>

[:material-email: Email](mailto:sayedshaun4@gmail.com){ .md-button }
[:fontawesome-brands-github: GitHub](https://github.com/sayedshaun){ .md-button }
[:fontawesome-brands-linkedin: LinkedIn](https://linkedin.com/in/sayed-shaun){ .md-button }
[:material-file-document: Résumé](files/resume.pdf){ .md-button target="_blank" rel="noopener" }

<nav class="page-nav" markdown>
[About](#about) ·
[Experience](#experience) ·
[Education](#education) ·
[Skills](#skills) ·
[Research](#research) ·
[Projects](#projects) ·
[Certifications](#certifications) ·
[Contact](#contact)
</nav>

## About

I came to machine learning through software engineering, and it still shows in how I work.
The modelling is rarely the hard part — the hard part is the data pipeline nobody documented,
the inference bill nobody forecast, and the evaluation that quietly stopped measuring anything
real. That's the half of the job I've ended up specialising in.

Day to day that means agentic systems — LLMs that call tools, route across databases, and
hold up under real traffic — plus the optimisation work that makes them affordable to run.
I also do research in low-resource NLP, which is where my published work sits, and I'm
preparing for a master's to push further into both.

### At a glance

| | |
|---|---|
| **Current role** | AI Engineer @ Synesis IT PLC |
| **Location** | Dhaka, Bangladesh |
| **Focus** | LLM · agentic AI · retrieval systems |
| **Education** | B.Sc. Computer Science & Engineering |
| **Publication** | BanSuite (EACL 2026) |
| **Looking for** | AI/ML engineering roles, research collaborations, master's programmes |

## Experience

<div class="grid cards stack" markdown>

-   **AI Engineer**

    ---

    Synesis IT PLC · Jun 2026 — present · Dhaka, Bangladesh
    { .meta }

    - Research and implement optimisation techniques for small and large language models — quantisation among them — to cut inference latency, shrink model size, and make deployment cheaper.
    - Design and integrate LLM-driven features into **Convay**, an online meeting platform, turning meetings into something searchable and actionable.

-   **Machine Learning Engineer**

    ---

    Giga Tech Limited · Sep 2024 — Jun 2026 · Dhaka, Bangladesh
    { .meta }

    - Built an AI-powered web crawler that extracts structured and unstructured data from wildly different websites, using adaptive parsing and LLM-based content understanding.
    - Built an agentic RAG chatbot for HR that resolved **90%** of employee queries across SQL and vector databases with open-source models.
    - Pretrained and fine-tuned Bangla language models — BERT, GPT, T5, LLaMA — on in-house corpora, improving **NER by 7.14%**, **POS tagging by 4.64%**, and **QA by 5.00%**.

-   **Trainee Software Engineer**

    ---

    Syntax Solution Limited · Jun 2024 — Aug 2024 · Dhaka, Bangladesh
    { .meta }

    - Replaced keyword search in a recommendation engine with a hybrid semantic + keyword architecture, a **25%** quality improvement.
    - Shipped a retrieval-augmented chatbot pipeline for repetitive queries that lifted customer interaction by roughly **37%**.

</div>

## Education

<div class="grid cards stack" markdown>

-   **B.Sc. in Computer Science & Engineering**

    ---

    World University of Bangladesh · Dhaka
    { .meta }

    Algorithms, data structures, databases, and software design — the engineering foundation
    that everything since has been built on.

    **Thesis:** *Advancement in Neuroimaging: Automated Identification of Brain Strokes through
    Machine Learning*
    { .meta }

</div>

!!! note "Currently preparing for a master's degree"

    I'm preparing to pursue a master's programme to deepen my research in low-resource NLP and
    scalable machine learning systems.

## Skills

<div class="grid cards stack" markdown>

-   :material-code-braces:{ .lg .middle } **Languages**

    ---

    :simple-python: Python · :simple-rust: Rust · :material-database-outline: SQL · :simple-gnubash: Bash

-   :material-brain:{ .lg .middle } **Modelling**

    ---

    :simple-pytorch: PyTorch · :simple-tensorflow: TensorFlow · :material-function-variant: JAX · :simple-huggingface: Transformers · :simple-huggingface: Hugging Face · :simple-numpy: NumPy

-   :material-rocket-launch-outline:{ .lg .middle } **Serving**

    ---

    :material-flash-outline: vLLM · :material-cube-outline: llama.cpp · :simple-nvidia: Triton Inference Server · :simple-onnx: ONNX

-   :material-server-outline:{ .lg .middle } **Backend**

    ---

    :simple-fastapi: FastAPI

-   :material-table-large:{ .lg .middle } **Data processing**

    ---

    :simple-pandas: Pandas · :simple-polars: Polars

-   :material-database-outline:{ .lg .middle } **Database**

    ---

    :simple-postgresql: PostgreSQL · :simple-mongodb: MongoDB · :material-vector-square: VectorDB

-   :material-infinity:{ .lg .middle } **MLOps / DevOps**

    ---

    :simple-docker: Docker · :simple-githubactions: CI/CD

</div>

## Research

<div class="grid cards stack" markdown>

-   **BanSuite: A Unified Toolkit and Software Platform for Low-Resource NLP in Bangla**

    ---

    EACL 2026 · System Demonstrations · 19th Conference of the European Chapter of the ACL
    { .meta }

    Md Abu Sayed, Faisal Ahamed Khan, Jannatul Ferdous Tuli, Nabeel Mohammed,
    Mohammad Ruhul Amin, Mohammad Mamun Or Rashid.

    A Bangla NLP platform bringing POS tagging, NER, shallow parsing, and dependency parsing
    under one roof, trained on a large manually-annotated treebank — around 90% F1/UAS, ahead
    of existing Bangla systems and general multilingual LLMs.

    [:material-file-document-outline: Read the paper](https://aclanthology.org/2026.eacl-demo.44/)

</div>

### Research interests

- **Multi-agent systems** — coordination, delegation, and control across many agents
- **AI agents** — tool use, planning, memory, and reliability under real workloads
- **Large language models** — training, adaptation, and efficient inference
- **AGI** — generalisation and reasoning beyond narrow, task-specific systems

## Projects

<div class="grid cards stack" markdown>

-   :material-graph-outline:{ .lg .middle } **Subagents**

    ---

    A lightweight framework for wiring plain Python functions — and the agents inside them —
    into a graph that runs branches in parallel, routes on conditions, and threads one typed
    state object through the whole thing.

    `Python` · `agent orchestration`

    [:octicons-mark-github-16: Repository](https://github.com/sayedshaun/subagents) ·
    [:octicons-book-16: Docs](https://sayedshaun.github.io/subagents/)

-   :material-spider-web:{ .lg .middle } **OneCrawler**

    ---

    An async crawling library with sitemap discovery, browser-based extraction, and LLM-powered
    structured output — all driven by a single Settings object instead of a config maze.

    `Python` · `asyncio` · `LLM extraction`

    [:octicons-mark-github-16: Repository](https://github.com/sayedshaun/onecrawler)

-   :material-api:{ .lg .middle } **OneCrawler Backend**

    ---

    The service that turns the library into a platform: a REST API for auth, crawl jobs,
    settings and extracted data, with the crawling handed to an async job queue.

    `Python` · `FastAPI` · `job queue`

    [:octicons-mark-github-16: Repository](https://github.com/sayedshaun/onecrawler-backend)

-   :material-fire:{ .lg .middle } **LangTrain**

    ---

    A PyTorch-backed package for rapid language-model development: large-scale tokenisation,
    distributed training, and evaluation without rebuilding the same scaffolding every time.

    `Python` · `PyTorch` · `distributed`

    [:octicons-mark-github-16: Repository](https://github.com/sayedshaun/langtrain)

-   :material-alphabetical-variant:{ .lg .middle } **WSD**

    ---

    A dual-architecture pipeline for training and evaluating Word Sense Disambiguation models,
    shipped with pretrained weights so you can start from a working baseline.

    `Python` · `PyTorch` · `pretrained weights`

    [:octicons-mark-github-16: Repository](https://github.com/sayedshaun/wsd)

-   :material-database-outline:{ .lg .middle } **Corpus**

    ---

    Bangladesh's national Bangla NLP platform — corpus development, syntactic annotation,
    low-resource language models, and the downstream tasks built on top of them.

    `Bangla NLP` · `core contributor`

    [:octicons-link-external-16: corpus.bangla.gov.bd](https://corpus.bangla.gov.bd)

-   :material-chat-processing-outline:{ .lg .middle } **ChatDocs**

    ---

    A private, self-hosted RAG chatbot for chatting with your own documents — built on
    LangChain and LangGraph, with a FastAPI backend and a ChromaDB + PostgreSQL storage layer,
    shipped as a Dockerised stack.

    `Python` · `LangGraph` · `RAG` · `FastAPI`

    [:octicons-mark-github-16: Repository](https://github.com/sayedshaun/chat-docs)

</div>

## Certifications

Verified coursework, most relevant first. Every entry links to its Coursera credential.

<div class="grid cards stack" markdown>

-   :simple-coursera:{ .lg .middle } **Generative AI with Large Language Models**

    ---

    Transformer architecture end to end, instruction fine-tuning, RLHF, and the deployment
    economics of running large models in production.

    `Coursera` · `DeepLearning.AI` · `Amazon Web Services`

    [:material-check-decagram: Verify](https://www.coursera.org/account/accomplishments/verify/F3MRR42W9ZQC)

-   :simple-coursera:{ .lg .middle } **DeepLearning.AI TensorFlow Developer**

    ---

    Building and training neural networks in TensorFlow across computer vision, natural
    language processing, and sequence models.

    `Coursera` · `DeepLearning.AI` · `Professional Certificate`

    [:material-check-decagram: Verify](https://www.coursera.org/account/accomplishments/professional-cert/E6SVAQQYNY4U)

-   :simple-coursera:{ .lg .middle } **Transformer Models and BERT Model**

    ---

    Self-attention and the transformer stack, and how BERT is pretrained and adapted to
    downstream tasks.

    `Coursera` · `Google Cloud`

    [:material-check-decagram: Verify](https://www.coursera.org/account/accomplishments/records/6D4TQ5L6HBJ7)

-   :simple-coursera:{ .lg .middle } **Machine Learning Specialization**

    ---

    The three-course specialization covering supervised and unsupervised learning, neural
    networks, and the judgement calls behind model selection and evaluation.

    `Coursera` · `DeepLearning.AI` · `Stanford Online`

    [Supervised Machine Learning: Regression and Classification](https://www.coursera.org/account/accomplishments/verify/WUW82VBGKY7E) ·
    [Advanced Learning Algorithms](https://www.coursera.org/account/accomplishments/verify/G8AKMGFLSVR5) ·
    [Unsupervised Learning, Recommenders, Reinforcement Learning](https://www.coursera.org/account/accomplishments/verify/5J7A782GDZCG)

    [:material-check-decagram: Verify specialization](https://www.coursera.org/account/accomplishments/specialization/QJCRTD63TRC2)

-   :simple-coursera:{ .lg .middle } **Mathematics for Machine Learning and Data Science**

    ---

    The mathematical groundwork under the models — matrices and transformations, gradients
    and optimisation.

    `Coursera` · `DeepLearning.AI`

    [Linear Algebra for Machine Learning and Data Science](https://www.coursera.org/account/accomplishments/verify/TT4CZEV8F5VB) ·
    [Calculus for Machine Learning and Data Science](https://www.coursera.org/account/accomplishments/verify/5KTNC8QUYV33)

-   :simple-coursera:{ .lg .middle } **Data Visualization with Python**

    ---

    Building charts and dashboards in Matplotlib, Seaborn, Plotly and Folium, and choosing
    the right form for the data at hand.

    `Coursera` · `IBM`

    [:material-check-decagram: Verify](https://www.coursera.org/account/accomplishments/verify/EELDXXPW2BTN)

-   :simple-udemy:{ .lg .middle } **Master Git and Github: Beginner to Expert**

    ---

    Version control end to end — branching and merging, resolving conflicts, and the
    collaboration workflows teams actually run on GitHub.

    `Udemy` · `Anisul Islam`

    [:material-check-decagram: Verify](https://www.udemy.com/certificate/UC-c37cf3f7-9413-482d-a9a7-9ef3cda1d342/)

-   :simple-coursera:{ .lg .middle } **Finding Your Professional Voice: Confidence & Impact**

    ---

    Communication and presentation skills — useful for the half of engineering that
    involves explaining the work to other people.

    `Coursera` · `University of London`

    [:material-check-decagram: Verify](https://www.coursera.org/account/accomplishments/records/WRDMXBAPKBVE)

</div>

## Contact

Open to AI/ML engineering roles, research collaborations, and master's programmes.
The fastest way to reach me is email.

[:material-email: sayedshaun4@gmail.com](mailto:sayedshaun4@gmail.com){ .md-button .md-button--primary } · [:fontawesome-brands-github: GitHub](https://github.com/sayedshaun){ .md-button } · [:fontawesome-brands-linkedin: LinkedIn](https://linkedin.com/in/sayed-shaun){ .md-button } · [:simple-huggingface: Hugging Face](https://huggingface.co/SayedShaun){ .md-button }
