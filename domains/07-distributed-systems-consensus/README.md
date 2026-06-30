# Track 07 · Distributed Systems & Consensus

> **Goal:** Build systems that are correct under partial failure. Understand consensus protocols at the implementation level, not just the theory.

---

## Why It Matters

Every large-scale system is a distributed system. The hard problems — split-brain, replication lag, stale reads, network partitions — are consensus problems in disguise. Engineers who have implemented Raft understand, on a visceral level, why Zookeeper, etcd, and Spanner make the decisions they do. This depth is what separates senior engineers who design for reliability from those who hope for it.

---

## Core Knowledge

**Distributed System Fundamentals**
- Fallacies of distributed computing (Deutsch's 8) — internalizing these changes how you design
- Time in distributed systems: physical clocks, NTP skew, logical clocks
- Lamport timestamps, vector clocks — causality tracking
- The FLP impossibility result — why consensus is hard
- CAP theorem (correctly understood) + PACELC as a more complete model

**Consensus Protocols**
- Paxos: single-decree, multi-Paxos, practical challenges
- Raft: leader election, log replication, safety proof, log compaction (snapshot), cluster membership changes
- Viewstamped Replication (historical context)
- Multi-Raft (used in TiKV, CockroachDB) — sharding with per-shard Raft groups
- Zookeeper atomic broadcast (ZAB) vs. Raft

**Consistency Models**
- Linearizability, sequential consistency, causal consistency, read-your-writes, eventual consistency
- How to think about consistency as a spectrum of guarantees with trade-offs
- Session guarantees in distributed KV stores

**Distributed Transactions**
- Two-Phase Commit (2PC): coordinator failure, blocking behavior
- Three-Phase Commit (3PC) and why it's not used in practice
- Saga pattern: choreography vs. orchestration, compensating transactions
- Percolator (Google's distributed transaction model — used in TiKV)

**Fault Tolerance Patterns**
- Quorum reads and writes (ROWA, quorum intersection)
- Hinted handoff, read repair, anti-entropy in leaderless systems (Dynamo-style)
- Failure detectors: φ-accrual failure detector
- Bulkheads, circuit breakers, timeouts in distributed service calls

**CRDTs & Conflict-Free Replication**
- CRDT types: G-Counter, PN-Counter, LWW-Register, OR-Set, MV-Register
- When CRDTs are the right tool (collaborative editing, geo-replication without coordination)

---

## How to Practice

1. **Implement Raft from scratch** — MIT 6.824 Lab 2 (Raft) is mandatory; do it in Go or Rust without reading others' implementations
2. **Implement a distributed KV store on top of your Raft** — MIT 6.824 Lab 3 (fault-tolerant KV)
3. **Read landmark papers** — Dynamo, Spanner, Zookeeper, CRAQ, Percolator (one per 2 weeks)
4. **Implement a G-Counter CRDT** — understand the merge semantics
5. **Run Jepsen-style tests** — inject network partitions into your KV store and verify linearizability with `elle`

---

## Deliverables

| Deliverable | Description |
|---|---|
| Raft implementation | Fully functional Raft with leader election + log replication + snapshots |
| Distributed KV store | Built on top of Raft, supports concurrent clients |
| CRDT implementation | PN-Counter and OR-Set with correctness tests |
| Paper reading notes | 5 papers with "why does this design choice exist?" annotations |

---

## Resources

- MIT 6.824 Distributed Systems (lectures + labs — free online)
- *Designing Data-Intensive Applications* ch. 5, 7, 8, 9 — best narrative intro
- Raft paper: "In Search of an Understandable Consensus Algorithm" — Ongaro & Ousterhout
- Jepsen.io — distributed systems correctness analyses
- TLA+ (temporal logic) — for formal verification of your protocol design
