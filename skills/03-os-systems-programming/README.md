# Track 03 · OS Internals & Systems Programming

> **Goal:** Understand the substrate that everything else runs on. Write systems-level code that is correct, efficient, and safe. Speak fluently about what happens below the framework.

---

## Why It Matters

Senior engineers at Google working on infrastructure, storage, networking, or security need OS-level intuition. In interviews, this knowledge sharpens your system design reasoning (why does disk I/O dominate? what is a context switch overhead?). In practice, it is the difference between guessing at a performance issue and diagnosing it.

---

## Core Knowledge

**Process & Thread Model**
- Process vs. thread vs. goroutine vs. coroutine — scheduling semantics
- Context switching cost, thread states, preemptive vs. cooperative scheduling
- Signals, process groups, job control
- `fork()`/`exec()` semantics, copy-on-write

**Memory Management**
- Virtual memory, page tables, TLB
- Physical vs. virtual address translation
- Memory-mapped files (`mmap`)
- Heap allocator internals (slab, buddy system)
- Stack growth, stack overflow, guard pages
- NUMA awareness in high-performance systems

**Concurrency Primitives**
- Mutex, semaphore, condition variable — correct usage and pitfalls
- Lock-free data structures (atomic CAS, ABA problem)
- Memory ordering models (acquire/release, sequentially consistent)
- Deadlock detection and avoidance

**I/O & Storage**
- Blocking vs. non-blocking vs. async I/O
- `epoll`/`kqueue`/`io_uring` — event-driven I/O models
- Page cache and buffer cache
- Filesystem internals: inode, dentry, VFS layer
- Direct I/O vs. buffered I/O

**Systems Programming (Rust-first)**
- Rust ownership model as a systems correctness tool
- Unsafe Rust — when and how to use it correctly
- FFI to C, linking, symbol resolution
- Writing a safe abstraction over an unsafe primitive
- `perf`, `strace`, `valgrind`, `flamegraph` — profiling toolchain

---

## How to Practice

1. **Implement from scratch:** a user-space thread scheduler, a memory allocator (`malloc`/`free`), a simple shell with pipe/redirect support
2. **Use perf to profile** a real program — identify hotspots and explain them at the OS level
3. **Read xv6** (MIT's teaching OS) — understand each subsystem end-to-end
4. **Rust systems project** — build something real: a file watcher, a ring buffer, a safe wrapper around a Linux API
5. **Use `strace` and `ltrace`** to trace real programs — demystify what your tools actually do

---

## Deliverables

| Deliverable | Description |
|---|---|
| Rust systems project | Crate published to crates.io or documented on GitHub |
| `malloc` implementation | Working heap allocator with basic free-list coalescing |
| OS internals writeup series | 3–5 deep-dive posts: scheduler, virtual memory, I/O |
| Profiling lab | Flamegraph + analysis of a real performance bottleneck |

---

## Resources

- *Operating Systems: Three Easy Pieces* (OSTEP) — free online, best OS textbook
- xv6 source code + MIT 6.S081 labs
- *Programming Rust* — Jim Blandy — systems Rust
- Linux kernel source (start with `fs/` or `mm/`)
- Brendan Gregg's *Systems Performance* — production profiling bible
