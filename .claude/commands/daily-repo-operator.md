# daily-repo-operator

Repo workflow operator for `tzc-engineering-growth-system`. Translates one Chinese sentence into a complete daily log cycle: file creation, content fill, git add/commit/push.

This skill operates only within this repository. It does not give general advice.

---

## When to Invoke

Trigger when the user says anything in Chinese that describes:
- Planning or starting the day
- Wrapping up or wanting to push
- Reporting what was done mid-session

**Examples:**
- "今天要做 TPM key hierarchy 設計"
- "幫我開始今天，今天打算做書本第二章"
- "今天做完了，幫我 push"
- "剛完成 SRK 設計筆記，記錄一下"
- "今天到這裡，收工"

---

## Step 0 — Always Do First

1. Run `date +%Y-%m-%d` to get today's date.
2. Determine intent from the user's sentence:
   - **start**: user is planning or starting the day → run Start-of-Day workflow
   - **end / push**: user is wrapping up → run End-of-Day workflow
   - **progress**: user is reporting a mid-session update → run Progress workflow

---

## Workflow A — Start of Day

**Goal:** Create `logs/YYYY-MM-DD.md`, sync to `TODAY.md`, commit, push.

### Steps

1. Read `NOW/focus.md` to identify the current active track.
2. Infer from the user's sentence:
   - **Day mode**: use Inference — Day Mode table below (default: Normal)
   - **Main track**: use Inference — Track table below
   - **Micro-goal**: extract verbatim from user's sentence; if absent, ask "今天的微目標是什麼？（一句話）"
   - **Problem-solving**: fill from user's input; if not mentioned, leave as template blanks
3. Write `logs/YYYY-MM-DD.md` using the template below.
4. Overwrite `TODAY.md` with identical content.
5. Run:
   ```
   git add logs/YYYY-MM-DD.md TODAY.md
   git commit -m "daily: YYYY-MM-DD start (plan)"
   git push origin main
   ```

### Log File Template

```markdown
# 今天 — YYYY-MM-DD

**今天的模式：** [fill based on inference]

---

## 解題練習 — 每天必做

- **來源：** [fill or leave as template]
- **題目 ID / 章節：** ___
- **題目名稱：** ___
- **Pattern：** ___
- **花費時間：** ___
- **結果：** `[ ] 獨立解出` `[ ] 看提示後解出` `[ ] 看解答理解`
- **核心洞察（一句話）：** ___

---

## 主技能 — 從 `NOW/focus.md` 選一條

**Track：** [inferred track path]
**今天的微目標（一句話）：** [from user input]

**做了什麼：**
-

**卡住的地方：**
-

---

## 產出 — 一個小東西

- [ ] ___

---

## 完成條件

- [ ] 解題：1 題做完並記錄
- [ ] 技能：focused session（Normal/Deep: 30 min+；Minimum: 任意長度）
- [ ] 產出：1 個東西歸檔

---

## 備註 / 阻礙

-

---

*只能做一件事的話：做解題練習。*
*有兩小時：解題 + 技能 session。*
*有四小時以上：解題 + 深度工作 + 寫點什麼。*
```

---

## Workflow B — End of Day / Push

**Goal:** Update `logs/YYYY-MM-DD.md` with actual results, sync to `TODAY.md`, commit, push.

### Steps

1. Read `logs/YYYY-MM-DD.md`.
2. Update from user's completion report:
   - Fill "做了什麼" bullets from what the user described
   - Fill "卡住的地方" from any blockers mentioned
   - Mark completed outputs with `[x]` and add actual file path
   - Mark completion checkboxes `[x]` for completed items
3. If the user mentions creating a note or document:
   - If title is unclear, ask: "這份筆記的標題是什麼？（短短幾個字）"
   - Create the note file at the correct path using the File Routing table
   - Append a row to `OUTPUTS/README.md` output log table
4. Overwrite `TODAY.md` with the updated log content.
5. Run:
   ```
   git add -A
   git commit -m "daily: YYYY-MM-DD progress (<summary>)"
   git push origin main
   ```
   - summary: English, ≤ 50 chars, describes what was actually done
   - Example: `daily: 2026-04-02 progress (TPM SRK key hierarchy design note)`

---

## Workflow C — Progress Update (mid-session)

Same as Workflow B, but lighter:
- Update only "做了什麼" and "卡住的地方"
- Do not touch completion checkboxes unless explicitly done
- Commit message: `daily: YYYY-MM-DD progress (<summary>)`
- Push.

---

## File Routing Table

When the user mentions creating a note or document, route it here:

| Topic keywords | Destination |
|---|---|
| TPM, attestation, key hierarchy, EK, AK, SRK, PKI, FIDO, TEE, secure boot | `NOTES/security/` |
| system design, distributed, cache, sharding, rate limiter, URL shortener | `NOTES/systems/` |
| OS, scheduler, memory, virtual memory, process, mmap, inode | `NOTES/systems/` |
| LLM, inference, RAG, vLLM, embedding, agent, prompt | `NOTES/misc/` |
| network, TCP, TLS, HTTP, gRPC, QUIC | `NOTES/systems/` |
| Full architecture or design documents (RFC-quality) | `OUTPUTS/designs/` |
| Technical writeups (blog-quality) | `OUTPUTS/writeups/` |
| Paper reading notes | `OUTPUTS/papers/` |
| Code implementations or project POCs | `OUTPUTS/projects/` |
| Everything else | `NOTES/misc/` |

**Filename convention:** `YYYY-MM-DD-short-topic-slug.md`

Example: `2026-04-02-tpm-agent-srk-redesign.md`

---

## Inference — Track

Infer the main track from keywords in the user's input. Do not ask.

| Keywords | Track |
|---|---|
| TPM, SRK, EK, AK, attestation, DevID, PKI, key hierarchy, FIDO, TEE, hardware trust | `SKILLS/05-security-trusted-systems/` |
| LeetCode, 刷題, 解題, array, DP, BFS, DFS, tree, graph, 書本題 | `SKILLS/01-dsa-coding-interview/` |
| system design, 系統設計, cache, sharding, rate limiter, URL shortener | `SKILLS/02-system-design-large-scale/` |
| OS, scheduler, memory, mmap, virtual memory, xv6 | `SKILLS/03-os-systems-programming/` |
| database, B-tree, LSM, MVCC, transaction, KV store | `SKILLS/04-database-internals-storage/` |
| TCP, TLS, HTTP, gRPC, QUIC, protocol, socket | `SKILLS/06-network-protocol-engineering/` |
| Raft, Paxos, consensus, distributed, CRDT, MIT 6.824 | `SKILLS/07-distributed-systems-consensus/` |
| LLM, inference, RAG, vLLM, embedding, agent, on-prem AI | `SKILLS/08-ai-llm-systems/` |
| k8s, kubernetes, container, helm, GitOps, operator | `SKILLS/09-cloud-native-platform/` |

If no keyword matches, read `NOW/focus.md` and use the first active track.

---

## Inference — Day Mode

| User signals | Mode to set |
|---|---|
| "忙"、"快速"、"只有一點時間"、"簡單做" | `[x] Minimum` |
| "週末"、"完整時間"、"衝刺"、"深度" | `[x] Deep` |
| No signal / default | `[x] Normal` |

---

## Git Commit Rules

| Situation | Format |
|---|---|
| Start of day | `daily: YYYY-MM-DD start (plan)` |
| Progress or end of day | `daily: YYYY-MM-DD progress (<summary>)` |

- summary: English, ≤ 50 chars
- Never mix daily log commits with skill track edits, README changes, or system restructuring
- If a note file is created, include it in the same progress commit — do not create a separate commit

---

## Ask At Most One Question

Do not ask multiple questions in one turn. If something is unclear, ask the one most critical missing piece:

1. "今天主要做什麼？" — if you have no idea what the session is about
2. "這份筆記的標題是什麼？" — if a note needs to be created but title is missing

Do not ask about track (infer it). Do not ask about day mode (infer it).

---

## TODAY.md Sync Rule

`TODAY.md` always mirrors the current day's `logs/YYYY-MM-DD.md`. After every write, overwrite `TODAY.md` with the same content. The two files are always identical for the current day.
