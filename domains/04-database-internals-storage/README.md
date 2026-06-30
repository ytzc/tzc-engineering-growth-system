# Track 04 · Database Internals & Storage

> **Goal:** Understand how databases work beneath the SQL, not just how to use them. Design storage layers that are correct, fast, and durable at scale.

---

## Why It Matters

Every system design interview touches databases. Candidates who understand indexing, transaction isolation, and replication at the implementation level make substantially better trade-off decisions. This depth also translates directly into building storage components for your own systems.

---

## Core Knowledge

**Storage Structures**
- B-tree and B+ tree: insertion, deletion, page splits, fill factor
- LSM-tree: MemTable, SSTable, compaction strategies (leveled, tiered), bloom filters
- WAL (Write-Ahead Log): crash recovery, checkpointing, ARIES algorithm
- Row stores vs. column stores — when and why

**Transaction Internals**
- ACID: atomicity, consistency, isolation, durability — what each actually requires
- MVCC: version chains, garbage collection, snapshot isolation
- Isolation levels: read uncommitted → serializable — what anomalies each prevents
- 2PL (Two-Phase Locking) vs. MVCC — trade-offs in practice
- Deadlock detection and prevention

**Query Execution**
- Query parsing, planning, and optimization pipeline
- Cost-based optimizer, statistics, and histograms
- Join algorithms: nested loop, hash join, sort-merge join
- Index types: B-tree, hash, GiST, partial, covering indexes
- Explain plan analysis — reading and acting on query plans

**Replication & Distributed Consistency**
- Single-leader vs. multi-leader vs. leaderless replication
- Replication lag and read-your-writes consistency
- Semi-synchronous vs. asynchronous replication
- Conflict resolution in multi-leader setups (last-write-wins, CRDTs)

**Modern Database Systems**
- PostgreSQL internals (buffer pool, VACUUM, autovacuum)
- RocksDB / LevelDB as embedded storage engines
- ClickHouse / column-store analytics engines
- Redis persistence modes (RDB, AOF)
- Vector databases (HNSW index, approximate nearest neighbor)

---

## How to Practice

1. **Read CMU 15-445** (Database Systems) — complete the programming projects (Buffer Pool Manager, B+ Tree, Query Executor)
2. **Implement a KV store** — start with log-structured storage, add an index, add compaction
3. **Analyze PostgreSQL behavior** — use `EXPLAIN ANALYZE` on real queries, observe buffer hit rates, index usage
4. **Paper reading** — Bigtable, Dynamo, Spanner, Aurora, Socrates
5. **Benchmark** — measure write amplification, read amplification, and space amplification for your KV store

---

## Deliverables

| Deliverable | Description |
|---|---|
| KV store implementation | LSM-tree based KV store in Rust or Go with benchmarks |
| CMU 15-445 projects | All 4 projects completed (buffer pool → query executor) |
| Query optimization case study | Real query plan before/after tuning with explanation |
| Paper reading notes | Bigtable + Dynamo with "what design decision surprised me" |

---

## Resources

- CMU 15-445 (free online with lecture videos and projects)
- *Designing Data-Intensive Applications* ch. 3–4 — storage engines
- *Database Internals* — Alex Petrov — deepest reference on storage
- PostgreSQL source code (`src/backend/storage/`)
- Papers: Bigtable (2006), Dynamo (2007), Spanner (2012)
