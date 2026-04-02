# daily-repo-operator

Repo workflow operator for `tzc-engineering-growth-system`. Translates one Chinese sentence into a complete daily log cycle using a two-phase inbox workflow: **start of day** (create inbox + log + today) and **end of day** (read inbox → classify → update records → git push).

This skill operates only within this repository. It does not give general advice.

---

## Core Concepts

Three files serve distinct roles. Never mix them.

| File | Role | Who writes it |
|---|---|---|
| `inbox/YYYY-MM-DD.md` | Raw materials — everything written during the day, unfiltered | User (during the day) |
| `logs/YYYY-MM-DD.md` | Official execution record — structured, final | Operator (at start + end of day) |
| `today.md` | Daily dashboard — always mirrors today's log | Operator (after every write to logs/) |

**inbox** is the only file the user needs to write during the day. It is preserved as-is. The operator reads it at end-of-day and distributes the content to the right places.

---

## When to Invoke

Trigger when the user says anything in Chinese that describes:
- Starting the day → run **Workflow A — Start of Day**
- Wrapping up or wanting to push → run **Workflow B — End of Day**
- Mid-session progress update → run **Workflow C — Progress Update**

**Start triggers:**
- "開始今天"、"幫我開始今天"、"今天開始"
- "今天 Normal day，要做 X"
- "幫我開始，今天打算做 Y"

**End triggers:**
- "今天結束"、"今天做完了"、"幫我收尾今天"、"收工"、"今天到這裡"、"幫我 push"

**Progress triggers:**
- "剛完成 X，記錄一下"、"先記一下進度"

---

## Step 0 — Always Do First

1. Run `date +%Y-%m-%d` to get today's date.
2. Determine intent (start / end / progress) from the user's sentence.

---

## Workflow A — Start of Day

**Goal:** Create `inbox/YYYY-MM-DD.md`, `logs/YYYY-MM-DD.md`, `today.md`. Commit and push.

### Steps

1. Read `NOW/focus.md` to identify the current active track.
2. Infer from the user's sentence:
   - **Day mode**: use Inference — Day Mode table (default: Normal)
   - **Main track**: use Inference — Track table
   - **Micro-goal**: extract verbatim from user's sentence; if absent, ask "今天的微目標是什麼？（一句話）"
   - **Problem-solving**: fill from user's input; if not mentioned, leave as template blanks
3. Create `inbox/YYYY-MM-DD.md` using the Inbox Template below.
4. Write `logs/YYYY-MM-DD.md` using the Log Template below.
5. Overwrite `today.md` with identical content to the log.
6. Run:
   ```
   git add inbox/YYYY-MM-DD.md logs/YYYY-MM-DD.md today.md
   git commit -m "daily: YYYY-MM-DD start (plan)"
   git push origin main
   ```

### Inbox Template

```markdown
# Inbox — YYYY-MM-DD

> 白天原始材料入口。想到什麼就寫在這裡，不需要整理。晚上由 Claude 幫你分類。

---

## 解題 / 書本題

<!-- 來源、題號、解法思路、卡住的地方、核心洞察 -->

---

## 技術思考 / 工作筆記

<!-- 任何 TPM、系統設計、架構想法、程式碼片段 -->

---

## 想記住的知識點

<!-- 值得背誦或做成記憶卡的內容 -->

---

## 書本重點

<!-- 閱讀時的摘錄或心得 -->

---

## 卡住的地方

<!-- 今天遇到的問題或阻礙 -->

---

## 明天下一步

<!-- 今天還沒做完，或想到明天要繼續的事 -->
```

### Log Template

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

## 主技能 — [inferred track path]

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

## Workflow B — End of Day

**Goal:** Read `inbox/YYYY-MM-DD.md`, classify its contents into the correct destinations, update `logs/YYYY-MM-DD.md` and `today.md`, update `progress/dashboard.md` if significant progress, commit and push.

### Steps

1. Read `inbox/YYYY-MM-DD.md`, `logs/YYYY-MM-DD.md`, `today.md`.
2. Classify inbox content and write to destinations (see Classification Rules below).
3. Update `logs/YYYY-MM-DD.md`:
   - Fill "做了什麼" bullets from what the user described in inbox
   - Fill "卡住的地方" from any blockers in inbox
   - Mark completed outputs with `[x]` and add actual file path
   - Mark completion checkboxes `[x]` for completed items
4. Overwrite `today.md` with updated log content.
5. If significant progress (new note, skill track pushed, problems solved), update `progress/dashboard.md`.
6. Run:
   ```
   git add -A
   git commit -m "daily: YYYY-MM-DD progress (<summary>)"
   git push origin main
   ```
   - summary: English, ≤ 50 chars, describes what was done
   - Example: `daily: 2026-04-02 progress (TPM SRK key hierarchy, C++ ch1)`

### Classification Rules

#### A. Problem Solving (解題 / 書本題)

If inbox contains any problem-solving entries → write to `leetcode/log/YYYY-MM-DD.md`.

Format:
```markdown
# 解題日誌 — YYYY-MM-DD

## [題目名稱 or 章節]

- **來源：** LeetCode / 書本：《書名》/ 其他
- **題目 ID / 章節：** ___
- **Pattern：** ___
- **花費時間：** ___
- **結果：** 獨立解出 / 看提示後解出 / 看解答理解
- **核心洞察：** ___
```

#### B. Technical Notes (技術思考 / 工作筆記)

Route using the File Routing Table. Create file at destination.
- Filename: `YYYY-MM-DD-short-topic-slug.md`
- Append a row to `OUTPUTS/README.md` output log table if the note is substantial (design-quality)

#### C. Memorizable Content (想記住的知識點)

If inbox has content suitable for active recall → write to `memorization/daily/YYYY-MM-DD.md`.

Format: Q&A pairs or fill-in-the-blank items, 5–10 minutes to review.

#### D. Unprocessed Remainder

Anything in inbox that doesn't fit a category: leave it in inbox. Do not force-classify.

**inbox is never deleted or modified by the operator.**

---

## Workflow C — Progress Update (mid-session)

Same as Workflow B, but lighter:
- Update only "做了什麼" and "卡住的地方" in the log
- Do not touch completion checkboxes unless user says something is done
- Do not update `progress/dashboard.md`
- Commit message: `daily: YYYY-MM-DD progress (<summary>)`
- Push.

---

## File Routing Table

| Topic keywords | Destination |
|---|---|
| TPM, attestation, key hierarchy, EK, AK, SRK, PKI, FIDO, TEE, TCG, secure boot, DevID | `NOTES/security/` |
| system design, distributed, cache, sharding, rate limiter, URL shortener | `NOTES/systems/` |
| OS, scheduler, memory, virtual memory, process, mmap, inode | `NOTES/systems/` |
| network, TCP, TLS, HTTP, gRPC, QUIC | `NOTES/systems/` |
| LLM, inference, RAG, vLLM, embedding, agent, prompt | `NOTES/misc/` |
| Full architecture or design documents (RFC-quality) | `OUTPUTS/designs/` |
| Technical writeups (blog-quality, publishable) | `OUTPUTS/writeups/` |
| Paper reading notes | `OUTPUTS/papers/` |
| Code implementations or project POCs | `OUTPUTS/projects/` |
| Everything else | `NOTES/misc/` |

**Filename convention:** `YYYY-MM-DD-short-topic-slug.md`

---

## Inference — Track

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

| User signals | Mode |
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
- If note files are created at end-of-day, include them in the same progress commit — do not create separate commits
- Stage specific files, not `git add -A`, unless end-of-day (where multiple classified files need staging)

---

## Ask At Most One Question

Do not ask multiple questions in one turn. If something is unclear, ask the one most critical missing piece:

1. "今天主要做什麼？" — if you have no idea what the session is about
2. "這份筆記的標題是什麼？" — if a note needs to be created but title is missing

Do not ask about track (infer it). Do not ask about day mode (infer it).

---

## TODAY.md Sync Rule

`today.md` always mirrors the current day's `logs/YYYY-MM-DD.md`. After every write, overwrite `today.md` with the same content. The two files are always identical for the current day.
