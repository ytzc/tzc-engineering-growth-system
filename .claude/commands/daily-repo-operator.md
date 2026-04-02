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
- Mid-session checkpoint (before end-of-day) → run **Workflow C — Progress Update**
- Resuming after end-of-day on the same calendar day → run **Workflow D — Resume Same Day**

**Start triggers:**
- "開始今天"、"幫我開始今天"、"今天開始"
- "今天 Normal day，要做 X"
- "幫我開始，今天打算做 Y"

**End triggers:**
- "今天結束"、"今天做完了"、"幫我收尾今天"、"收工"、"今天到這裡"、"幫我 push"

**Progress triggers (mid-session only, before End of Day):**
- "剛完成 X，記錄一下"、"先記一下進度"

**Resume triggers (after End of Day on the same day):**
- "我回來繼續今天的工作"
- "晚上回來補一下"
- "已經收工了但想再做一點"
- "幫我接著今天做"
- "我回來了，繼續今天"
- "收工後回來"

---

## Step 0 — Always Do First

1. Run `date +%Y-%m-%d` to get today's date.
2. Determine intent using the **Workflow Disambiguation Rule** below.

### Workflow Disambiguation Rule

Apply in order. Use the **first** rule that matches.

| Condition | Workflow |
|---|---|
| User says a Resume trigger | **D** — Resume Same Day |
| User says a Start trigger AND `logs/YYYY-MM-DD.md` does NOT exist | **A** — Start of Day |
| User says a Start trigger AND `logs/YYYY-MM-DD.md` already exists | **D** — Resume Same Day (do not recreate files) |
| User says an End trigger | **B** — End of Day |
| User says a Progress trigger | **C** — Progress Update |

**Key principle:** If today's files already exist and the user wants to continue, always use D. Never re-run A on a day that has already been started.

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
4. Create `assets/inbox/YYYY-MM-DD/` as today's asset staging area:
   ```
   mkdir -p assets/inbox/YYYY-MM-DD
   touch assets/inbox/YYYY-MM-DD/.gitkeep
   ```
5. Write `logs/YYYY-MM-DD.md` using the Log Template below.
6. Overwrite `today.md` with identical content to the log.
7. Run:
   ```
   git add inbox/YYYY-MM-DD.md logs/YYYY-MM-DD.md today.md assets/inbox/YYYY-MM-DD/.gitkeep
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

#### D. Assets (圖片 / 架構圖 / draw.io)

**Source directory:** `assets/inbox/YYYY-MM-DD/`

List the directory. If empty or absent, skip this section.

##### D1 — Routing Decision (per file)

For each file, determine: **route** (move to permanent location) or **hold** (leave in `assets/inbox/YYYY-MM-DD/`).

**Route if all of the following are true:**
- Topic is identifiable (from filename, or from adjacent text in `inbox/YYYY-MM-DD.md`)
- File is complete enough to be useful (not an empty placeholder, not a temp export)

**Hold (leave in place) if any of the following are true:**
- Filename gives no topic clue AND no inbox text describes it
- File appears to be an intermediate export (e.g., `Untitled.png`, `image001.png`)
- The drawio source file is present but has not been exported yet → hold the `.drawio`, do not force export

**When holding**, add one line to the log under "備註 / 阻礙":
```
`assets/inbox/YYYY-MM-DD/<filename>` — topic unclear, held for manual triage
```

##### D2 — Routing Rules

| File type | Destination |
|---|---|
| `.drawio` source file | `assets/diagrams/<topic>/YYYY-MM-DD-<slug>.drawio` |
| Exported `.png` / `.svg` / `.pdf` from draw.io | `assets/exports/<topic>/YYYY-MM-DD-<slug>.png` |
| Screenshot or raw sketch photo | `assets/exports/<topic>/YYYY-MM-DD-<slug>.png` |

- `<slug>` is a short lowercase kebab-case description inferred from filename or inbox context (e.g., `srk-key-hierarchy`, `cache-arch`)
- Create the destination directory if it does not exist: `mkdir -p assets/diagrams/<topic>` or `mkdir -p assets/exports/<topic>`
- Move with `mv`, do not copy

**Asset Topic Routing:**

| Keywords in filename or adjacent inbox text | Topic folder |
|---|---|
| tpm, srk, ek, ak, attestation, pki, fido, tee, secure-boot, devid | `security` |
| system-design, arch, cache, db, distributed, raft, kv, network, tcp | `systems` |
| llm, rag, inference, agent, embedding, vllm | `ai` |
| anything else | `misc` |

##### D3 — Note Image Linking

After routing, for each file moved to `assets/exports/<topic>/`:

1. Find the note that should reference this image. Candidates (in order of priority):
   - A note created today whose topic matches the asset topic
   - `inbox/YYYY-MM-DD.md` if no note was created (fallback)
2. Determine the **relative path** from the note file to the asset:
   - From `NOTES/security/YYYY-MM-DD-foo.md` → `../../assets/exports/security/YYYY-MM-DD-slug.png`
   - From `inbox/YYYY-MM-DD.md` → `../assets/exports/<topic>/YYYY-MM-DD-slug.png`
3. Insert the reference at the **bottom of the relevant section** in the note (not at the very end of the file):
   ```markdown
   ![<slug description>](<relative-path>)
   ```
4. If the note already contains an image reference to this file, skip — do not duplicate.

For `.drawio` files moved to `assets/diagrams/`, do NOT add an image reference (they are source files, not renderable images).

If no note matches and the inbox fallback is used, add the reference under a new `## 圖片` section at the bottom of the inbox file.

#### E. Unprocessed Remainder

Anything in inbox that doesn't fit a category: leave it in inbox. Do not force-classify.

**inbox and inbox/YYYY-MM-DD/ are never deleted by the operator. Only assets explicitly routed above are moved.**

---

## Workflow C — Progress Update (mid-session)

**Use only when:** the user wants a quick checkpoint *during* the working session, before End of Day has been run. If End of Day has already been run and the user is coming back to continue, use **Workflow D** instead.

### Steps

1. Read `inbox/YYYY-MM-DD.md` and `logs/YYYY-MM-DD.md`.
2. Append new bullets to "做了什麼" based on what the user described.
3. Update "卡住的地方" if new blockers are mentioned.
4. Do not touch completion checkboxes.
5. Do not update `progress/dashboard.md`.
6. Overwrite `today.md` with updated log content.
7. Run:
   ```
   git add logs/YYYY-MM-DD.md today.md
   git commit -m "daily: YYYY-MM-DD progress (<summary>)"
   git push origin main
   ```

---

## Workflow D — Resume Same Day

**Use when:** the user has already run End of Day (Workflow B) and is returning to continue work on the same calendar day. Do NOT re-run Workflow A. Do NOT recreate any files.

**Triggers:**
- "我回來繼續今天的工作"
- "晚上回來補一下"
- "已經收工了但想再做一點"
- "幫我接著今天做"
- "我回來了，繼續今天"
- "收工後回來"
- Any Start-of-day trigger where `logs/YYYY-MM-DD.md` already exists

### Steps

1. Read `inbox/YYYY-MM-DD.md`, `logs/YYYY-MM-DD.md`, `today.md`.
2. Append any new material the user brings to `inbox/YYYY-MM-DD.md` under the appropriate section. Do not overwrite existing content.
3. Update `logs/YYYY-MM-DD.md`:
   - Append new bullets to "做了什麼"
   - Update "卡住的地方" if new blockers are mentioned
   - Mark completion checkboxes `[x]` **only** if the user explicitly says something is done
   - If a new output file was produced, add it to "產出" and mark `[x]` with the file path
4. If new classifiable content exists in inbox (new technical note, problem-solving, memorizable content) — classify it using the Classification Rules from Workflow B.
5. Overwrite `today.md` with updated log content.
6. Run:
   ```
   git add -A
   git commit -m "daily: YYYY-MM-DD resume (<summary>)"
   git push origin main
   ```
   - summary: English, ≤ 50 chars
   - Example: `daily: 2026-04-02 resume (SRK key hierarchy diagram)`

### What Workflow D does NOT do

- Does NOT create `inbox/YYYY-MM-DD.md` (already exists)
- Does NOT create `logs/YYYY-MM-DD.md` (already exists)
- Does NOT create `assets/inbox/YYYY-MM-DD/` (already exists)
- Does NOT reset or overwrite existing log content — only appends
- Does NOT change the day mode or micro-goal unless user explicitly updates them

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
| Resume same day | `daily: YYYY-MM-DD resume (<summary>)` |

- summary: English, ≤ 50 chars
- Never mix daily log commits with skill track edits, README changes, or system restructuring
- If note files are created at end-of-day or resume, include them in the same commit — do not create separate commits
- Stage specific files, not `git add -A`, unless end-of-day or resume (where multiple classified files may need staging)

---

## Ask At Most One Question

Do not ask multiple questions in one turn. If something is unclear, ask the one most critical missing piece:

1. "今天主要做什麼？" — if you have no idea what the session is about
2. "這份筆記的標題是什麼？" — if a note needs to be created but title is missing

Do not ask about track (infer it). Do not ask about day mode (infer it).

---

## TODAY.md Sync Rule

`today.md` always mirrors the current day's `logs/YYYY-MM-DD.md`. After every write, overwrite `today.md` with the same content. The two files are always identical for the current day.
