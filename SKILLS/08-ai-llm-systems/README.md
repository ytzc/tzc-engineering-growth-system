# Track 08 · AI/LLM Systems Engineering

> **Goal:** Build production-grade AI infrastructure with security, performance, and operational rigor. Bridge the gap between model capability and system reliability. This is your second differentiator after Security.

---

## Why It Matters

The AI infrastructure layer is severely under-engineered relative to the demand. Most AI engineers can train models; very few can build the infrastructure that serves them securely, efficiently, and at scale. Your on-premise AI work gives you a head start — systematize it into transferable expertise.

The combination of LLM systems engineering + hardware security is a genuinely rare and valuable profile.

---

## Core Knowledge

**LLM Inference Fundamentals**
- Transformer architecture: attention mechanism, KV cache, why KV cache size scales with context length
- Batching strategies: static batching vs. continuous batching (PagedAttention)
- Quantization: FP16, INT8, INT4 — accuracy vs. latency vs. throughput trade-offs
- Speculative decoding — how it reduces latency for autoregressive generation
- Prefill vs. decode phases — the two bottlenecks and how to address each

**Inference Infrastructure**
- vLLM: PagedAttention, continuous batching, tensor parallelism
- Triton Inference Server — model ensemble, dynamic batching, protocol support
- ONNX Runtime — framework-agnostic model serving
- GPU memory management: VRAM budgeting, model sharding, pipeline parallelism
- Multi-GPU and multi-node inference: tensor parallelism, pipeline parallelism, expert parallelism (MoE)

**RAG Architecture**
- Chunking strategies: fixed-size, semantic, hierarchical
- Embedding models: dense (sentence-transformers), sparse (BM25), hybrid
- Vector databases: FAISS, Qdrant, Weaviate, pgvector — HNSW index internals
- Retrieval evaluation: recall@k, NDCG, RAGAs framework
- Advanced RAG: HyDE, query rewriting, contextual compression, re-ranking (cross-encoder)

**Agent Systems**
- Agent loop: plan → act → observe → reflect
- Tool use and function calling — OpenAI/Anthropic tool call APIs
- Multi-agent orchestration: supervisor pattern, handoff protocol
- Memory: in-context, external (vector store), structured (database)
- Reliability patterns: output validation, retry with backoff, human-in-the-loop escalation

**Secure & Private AI Infrastructure**
- On-premises LLM deployment: air-gap constraints, model weight protection
- Hardware-level model integrity verification (your existing work)
- Audit logging for AI inference: what was asked, what was returned, by whom
- Data residency and compliance constraints in AI systems
- Differential privacy in fine-tuning, federated learning basics

**Evaluation & Observability**
- LLM evaluation: BLEU, ROUGE, human eval, LLM-as-judge
- Drift detection: embedding drift, output distribution shift
- Latency profiling: time-to-first-token (TTFT), tokens-per-second (TPS)
- OpenTelemetry for AI pipelines — tracing inference requests end-to-end

---

## How to Practice

1. **Build a production RAG system** on your on-premise AI platform — with hybrid retrieval, re-ranking, and evaluation metrics
2. **Profile vLLM throughput** — measure how continuous batching and PagedAttention improve GPU utilization vs. naive serving
3. **Implement a minimal agent loop** — tool-using agent with memory and retry logic, without LangChain as a crutch
4. **Integrate attestation into your inference stack** — bind model serving to hardware attestation (extend your existing work)
5. **Read key papers** — Attention Is All You Need, FlashAttention, PagedAttention, Self-RAG, ReAct

---

## Deliverables

| Deliverable | Description |
|---|---|
| Production RAG system | End-to-end: ingest → chunk → embed → retrieve → generate → evaluate |
| Inference benchmark report | vLLM vs. naive serving: TTFT, TPS, GPU utilization at different batch sizes |
| Secure inference architecture doc | Design doc: how model integrity + audit + isolation works in your stack |
| Agent framework mini-project | Tool-using agent: custom tool, memory, retry, output validation |
| AI systems writeup | Blog-quality technical post on one of: secure inference, RAG evaluation, PagedAttention |

---

## Resources

- vLLM documentation and source code (PagedAttention paper)
- FlashAttention paper — Dao et al. (why attention is memory-bandwidth bound)
- *Building LLMs for Production* — Maxime Labonne (free online)
- Anthropic Engineering Blog — frontier AI systems thinking
- LlamaIndex and LangGraph documentation (understand the abstraction before using it)
- Simon Willison's weblog — best practitioner perspective on LLM systems
