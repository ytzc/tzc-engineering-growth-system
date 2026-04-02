# Track 02 · System Design — Large Scale

> **Goal:** Design any production system at Google/Meta scale with senior-level depth: capacity estimation, failure modes, consistency trade-offs, and operational concerns.

---

## Why It Matters

System Design interviews separate L4 from L5+ at Google. Candidates who pass are not just those who know the components — they are those who reason about trade-offs, justify decisions with constraints, and proactively surface failure modes. This track is also the most direct path to operating as a senior engineer day-to-day.

---

## Core Knowledge

**Fundamentals**
- CAP theorem, PACELC model — what they actually constrain in practice
- Strong consistency vs. eventual consistency vs. causal consistency
- Read-heavy vs. write-heavy system design patterns
- Latency / throughput / availability SLA reasoning

**Data Layer**
- Horizontal sharding (range, hash, consistent hashing)
- Replication strategies (primary-replica, multi-primary, quorum writes)
- Read replicas and replication lag handling
- Cache topologies: write-through, write-back, write-around, read-through
- Cache eviction: LRU, LFU, ARC

**Scalability Primitives**
- Load balancing (L4 vs. L7, consistent hashing ring)
- Rate limiting (token bucket, leaky bucket, sliding window counter)
- Message queues / event streaming (Kafka, pub-sub semantics, at-least-once vs. exactly-once)
- CDN and edge caching
- API gateway and service mesh basics

**Reliability Engineering**
- Single points of failure identification and elimination
- Circuit breakers, bulkheads, timeouts, retries with backoff
- Chaos engineering mindset (what if this node fails?)
- Graceful degradation vs. hard failure

**Advanced Topics (senior-level)**
- Geo-distribution and multi-region active-active
- Leader election (Zookeeper, etcd, Raft-based)
- Idempotency keys and exactly-once delivery
- Distributed transactions and saga pattern
- Observability: traces, metrics, logs correlation at scale

---

## How to Practice

1. **30-minute design sessions** — pick a system, timebox to 30 min, then critique your own design
2. **Classic systems to master:** URL shortener, Pastebin, Twitter feed, YouTube, Uber, Google Search, Dropbox, WhatsApp, Ticketmaster, distributed key-value store, rate limiter, notification system
3. **Read real engineering blogs** — Google SRE book, Stripe/Discord/Cloudflare engineering blogs
4. **Paper reading** — Spanner, Dynamo, Bigtable, Chubby, MapReduce (one per two weeks)
5. **Design critique** — review your own designs after 48h with fresh eyes and write down what you missed

---

## Deliverables

| Deliverable | Description |
|---|---|
| 10 design write-ups | Full markdown docs: requirements → components → trade-offs → failure modes |
| Capacity estimation template | Reusable QPS / storage / bandwidth estimation worksheet |
| Paper reading notes | Summary + "what surprised me" for 5 landmark papers |
| Design vocabulary doc | Personal glossary of terms used fluently in interviews |

---

## Resources

- *Designing Data-Intensive Applications* (DDIA) — Kleppmann — mandatory
- *System Design Interview* Vol. 1 & 2 — Alex Xu — interview format practice
- Google SRE Book (free online)
- ByteByteGo newsletter and YouTube channel
- Highscalability.com — real architecture case studies
