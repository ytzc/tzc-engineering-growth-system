# Track 06 · Network Engineering & Protocol Design

> **Goal:** Understand the network stack from Ethernet frames to application protocols. Design systems with realistic network failure models and reason precisely about latency, throughput, and security.

---

## Why It Matters

Networks are the connective tissue of distributed systems. Every performance optimization, every security boundary, every resilience mechanism is ultimately constrained by how data moves. Engineers who can reason from TCP behavior to application-level design make substantially better architectural decisions.

---

## Core Knowledge

**TCP/IP Stack**
- Ethernet, ARP, IP routing (CIDR, longest prefix match)
- TCP: three-way handshake, connection teardown, sequence numbers, ACKs
- TCP congestion control: slow start, congestion avoidance, fast retransmit/recovery, CUBIC, BBR
- UDP and when to choose it (latency-sensitive, loss-tolerant workloads)
- IP fragmentation, MTU, Path MTU Discovery

**TLS & Cryptographic Protocols**
- TLS 1.3: handshake flow, 0-RTT, session resumption
- Certificate validation, OCSP stapling, CT logs
- Cipher suites, forward secrecy (ECDHE), HKDF in TLS 1.3
- mTLS — mutual authentication in service-to-service communication

**Modern Application Protocols**
- HTTP/1.1 → HTTP/2 (multiplexing, HPACK, server push) → HTTP/3 (QUIC)
- QUIC internals: connection IDs, stream multiplexing, loss recovery without HOL blocking
- gRPC: protocol buffers, streaming modes, load balancing, deadlines
- WebSocket vs. SSE vs. long polling — when each is appropriate

**DNS & Service Discovery**
- DNS resolution chain: recursive resolver, authoritative NS, TTL
- DNS security: DNSSEC, DoH, DoT
- Service discovery patterns: DNS-SD, Consul, Kubernetes DNS

**Network Security**
- Firewall models: stateless, stateful, NGFW
- NAT traversal (STUN/TURN/ICE) — relevant for IoT and P2P
- DDoS mitigation patterns: anycast, rate limiting, SYN cookies
- Network segmentation and zero-trust network models
- WireGuard — modern VPN protocol internals

**Observability & Debugging**
- `tcpdump` / Wireshark — reading packet captures
- `ss`, `netstat`, `/proc/net/` — connection state inspection
- Network performance benchmarking: `iperf3`, `wrk`, `hey`

---

## How to Practice

1. **Implement an HTTP/1.1 server from scratch** in Rust — no frameworks, raw TCP sockets
2. **Capture and analyze** a real TLS handshake in Wireshark — annotate every packet
3. **Build a toy DNS resolver** — recursive resolver that handles A, AAAA, CNAME records
4. **Implement a chat protocol** over TCP with custom framing and reconnection logic
5. **WireGuard lab** — set up a WireGuard mesh network and trace the cryptographic key exchange

---

## Deliverables

| Deliverable | Description |
|---|---|
| Raw HTTP server | TCP socket-based HTTP/1.1 server in Rust, supports keep-alive |
| DNS resolver | Working recursive resolver in Python or Rust |
| Protocol deep-dive writeup | TLS 1.3 handshake annotated packet-by-packet |
| Network debugging runbook | Personal guide: how to diagnose latency, packet loss, TLS issues |

---

## Resources

- *Computer Networking: A Top-Down Approach* — Kurose & Ross
- Beej's Guide to Network Programming (free online)
- *High Performance Browser Networking* — Ilya Grigorik (free online) — HTTP/2 and QUIC
- Cloudflare blog — world-class network engineering writing
- Wireshark Sharks on the Wire (practical lab series)
- WireGuard whitepaper
