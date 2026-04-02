# tzc-engineering-growth-system
### *複利累積，長期主義。一個工程師的個人成長作業系統。*

---

## 這是什麼

這個 repository 是一套**個人工程師長期成長系統**。

它不是課程、不是 bootcamp、不是短期衝刺。它是一套**持續運作的作業系統**，將學習軌道、刷題、閱讀、技術筆記、記憶訓練、進度追蹤整合成一個可長期維護的結構。

設計原則只有一個：**可以持續一年以上地運作，而不是三天熱度。**

---

## 為什麼建立這套系統

技術能力的累積失敗，通常不是因為不努力，而是因為沒有結構。

- 學了忘、忘了再學，沒有複利
- 筆記散落各處，無法搜尋與回顧
- 每天做了事情，但進度不可見
- 沒有方向感，被短期需求拖著走

這套系統解決上述問題：
- 用**軌道制**管理十個技術方向，不讓任何一個落空
- 用**每日、每週、每月**的節奏讓知識真正沉澱
- 用**進度可視化**維持長期動力與方向感

---

## 核心原則

| 原則 | 說明 |
|---|---|
| **一致性優於強度** | 每天 30 分鐘，勝過週末 5 小時 |
| **複利思維** | 每天的輸入會累加，方向正確的話回報是指數型的 |
| **刻意練習** | 針對弱點訓練，而非一直重複熟悉的東西 |
| **深度優先** | 先把基礎吃透，再擴張廣度 |
| **全部記錄** | 洞察、失誤、邊界案例，都比整潔的摘要更有價值 |
| **回顧才算完成** | 學過不複習等於沒學，系統需要強制性的回顧機制 |

---

## Repository 結構

```
tzc-engineering-growth-system/
│
├── PLAN/                        # 主計畫、里程碑、長期目標
│   ├── master-plan.md
│   ├── milestones.md
│   └── vision.md
│
├── today.md                     # ← 每天操作面板。永遠與當天 logs/ 同步。
├── this_week.md                 # ← 週一設定，週日回顧。
│
├── inbox/                       # 白天原始材料入口（每天一個檔案，不整理）
│   └── YYYY-MM-DD.md            # 解題、技術思考、知識點、卡點，隨時寫
│
├── logs/                        # 每日執行歷史記錄（結構化，Claude 維護）
│   └── YYYY-MM-DD.md            # 每天一個檔案，today.md 鏡像
│
├── NOW/                         # 當前狀態 — 現在哪些 track 是 active
│   ├── focus.md                 # Active tracks 與當前 milestone
│   └── queue.md                 # 排隊中的 skill 和 output，按優先序
│
├── OUTPUTS/                     # 所有產出 — 你的 portfolio
│   ├── README.md                # 索引 + 十個月產出目標
│   ├── writeups/                # 技術文章、深度分析、部落格草稿
│   ├── designs/                 # System design 文件
│   ├── projects/                # 程式實作、POC、開源專案
│   ├── papers/                  # 論文閱讀筆記（含自己的分析）
│   └── talks/                   # 演講摘要、投影片、研討會投稿
│
├── SKILLS/                      # 10 個 skill track（面向 FAANG / 高階工程師）
│   ├── track-template.md        # 每個 track 的標準可執行格式
│   ├── 01-dsa-coding-interview/
│   ├── 02-system-design-large-scale/
│   ├── 03-os-systems-programming/
│   ├── 04-database-internals-storage/
│   ├── 05-security-trusted-systems/
│   ├── 06-network-protocol-engineering/
│   ├── 07-distributed-systems-consensus/
│   ├── 08-ai-llm-systems/
│   ├── 09-cloud-native-platform/
│   └── 10-engineering-impact-leadership/
│
├── LEETCODE/                    # 刷題日誌、題型整理、策略
│   ├── log/
│   ├── patterns/
│   └── strategy.md
│
├── READING/                     # 書單、閱讀筆記、書摘
│   ├── booklist.md
│   ├── notes/
│   └── summaries/
│
├── NOTES/                       # 技術深度筆記（依領域分類）
│   ├── systems/
│   ├── security/
│   ├── backend/
│   └── misc/
│
├── MEMORIZATION/                # 默寫卡、間隔重複內容
│   ├── daily/
│   └── index.md
│
├── REVIEWS/                     # 每週、每月回顧
│   ├── weekly/
│   └── monthly/
│
├── PROGRESS/                    # 進度儀表板、習慣追蹤
│   ├── dashboard.md
│   ├── habits.md
│   └── metrics/
│
└── RESUME/                      # 履歷（中英文版本、版本管理）
```

---

## 執行哲學

> 這不是學習課程，是一套工程師成長的作業系統。
> 系統失敗的原因只有一個：規劃取代了執行。

**規則一 — 產出優於消費。** 寫一份 design doc，比讀三個小時的書更有效。實作一個解法，比看教學影片更有效。每次 session 要產生一個東西：一篇筆記、一段程式碼、一個圖、一段文字。如果 `OUTPUTS/` 和 `NOTES/` 沒有增加，那次 session 沒有複利。

**規則二 — 最低執行勝過最優規劃。** 狀態差的日子，做最少版本就好。一週五題，勝過完美計畫加零次執行。

**規則三 — 每週調整，不是每月調整。** 面對明顯失敗訊號還死守計畫，是 bug，不是紀律。每個週日，調整。

**規則四 — 同時最多三個 active track。** DSA（永遠）+ 一個主技能 + 一個差異化方向。同時推進全部 10 個，等於每個都沒有真正深度。

**規則五 — feedback loop 勝過文件完整性。** 寫每週回顧。更新 dashboard。跳過回顧，你就是閉著眼睛在飛。

---

## 每日執行模式

三種模式，選符合今天實際狀況的那種，不要強行套用理想版本：

### Minimum Day（忙碌 / 低能量 / 出差）
> 一件事，不可跳過。
- 解題練習：1 題，解完記錄（30 分鐘）
- 有多餘時間：30 分鐘主技能 session

### Normal Day（一般工作日 + 晚上時段）
> 三件事。
- 解題練習：2–3 題（45–60 分鐘）
- 主技能：有焦點的 session，一個明確的微目標（60–90 分鐘）
- 產出：1 個小東西 → `NOTES/` 或 `OUTPUTS/`（30 分鐘）

### Deep Day（完整時間塊 / 假日 / 專注衝刺）
> 深入一件事。
- 解題練習：3–5 題，含一道 hard（60–90 分鐘）
- 主技能：build 或 write（2–4 小時）— 專案、文章、實作
- 產出：有份量的東西 → `OUTPUTS/`

**決策規則：** 打開 `TODAY.md`，宣告今天是哪種模式，填三個欄位，三個 checkbox 全打勾才算完成今天。

---

## 主線 vs 支線策略

十條 track 無法平行推進，全開等於全沒深度。

### 永遠在線的主線（每月、每週都要碰）
| Track | 為什麼永遠 active |
|---|---|
| 01 DSA & Coding Interview | 面試核心關卡 — 一致性才能累積 |
| 02 System Design — Large Scale | 第二個面試核心 — 深度需要數個月才能建立 |
| 05 Security & Trusted Systems | 你的主要差異化優勢 — 維持並持續深化 |

### 輪流支線（每月 1 條，從 `NOW/queue.md` 輪入）
第 3–8 月：OS → Network → Distributed Systems → Database → Security OSS → AI/LLM

### 背景模式（低頻接觸，以產出為主）
| Track | 說明 |
|---|---|
| 08 AI/LLM Systems | 第 7 月啟動 — 利用現有平台工作延伸 |
| 10 Engineering Impact | 第 5 月起 — 每月一篇 RFC 或技術文章 |

### 停放（排程到了再啟動）
其餘 track。啟動時間點見 `NOW/queue.md`。

---

---

## 10 個技術學習軌道

**設計原則：** 面向 Google / FAANG 面試 + 高階工程師能力，而非學校課程。

每個軌道放在 `SKILLS/XX-track-name/README.md`，包含：目標（why）、核心知識、練習方式、可交付成果。

| # | 軌道 | 核心定位 | 狀態 |
|---|---|---|---|
| 01 | [DSA & Coding Interview](SKILLS/01-dsa-coding-interview/) | 面試通關基礎，題型識別 | 🔵 進行中 |
| 02 | [System Design — Large Scale](SKILLS/02-system-design-large-scale/) | Senior level 系統設計 | 🔵 進行中 |
| 03 | [OS Internals & Systems Programming](SKILLS/03-os-systems-programming/) | 底層深度，Rust/C | ⬜ 待啟動 |
| 04 | [Database Internals & Storage](SKILLS/04-database-internals-storage/) | B-tree / LSM / MVCC | ⬜ 待啟動 |
| 05 | [Security & Trusted Systems](SKILLS/05-security-trusted-systems/) | **稀缺差異化** — TPM / TEE / Attestation | 🔵 進行中 |
| 06 | [Network Protocol Engineering](SKILLS/06-network-protocol-engineering/) | TCP/TLS/QUIC/gRPC | ⬜ 待啟動 |
| 07 | [Distributed Systems & Consensus](SKILLS/07-distributed-systems-consensus/) | Raft / Paxos / CRDT | ⬜ 待啟動 |
| 08 | [AI/LLM Systems Engineering](SKILLS/08-ai-llm-systems/) | **差異化** — RAG / Inference / Agents | 🔵 進行中 |
| 09 | [Cloud-Native & Platform Engineering](SKILLS/09-cloud-native-platform/) | k8s internals / SRE / GitOps | ⬜ 待啟動 |
| 10 | [Engineering Impact & Leadership](SKILLS/10-engineering-impact-leadership/) | RFC / 架構決策 / 工程影響力 | ⬜ 待啟動 |

> 同時間只深耕 2–3 個軌道，每月回顧時調整優先順序。

---

## 十個月執行策略

> 為在職工程師設計，不是為學生。預設你會有疲勞、中斷和 priority 變動。
> 計畫是指南，真正的調整發生在每週回顧。

### 四個 Phase

---

**Phase 1 — Foundation（第 1–2 月）**
*建立每日習慣。建立解題底子。把現有 security 知識系統化。*

- 解題練習：NeetCode 75 → LeetCode 150。以 pattern 為主，計時，每日記錄。（書本題目也算，不限平台。）
- System Design：打穩基礎（容量估算、caching、sharding、replication）。5 個基礎設計附書面筆記。
- Security：整理並文件化你現有的 TPM/FDO 專業。一篇可公開的技術文章。
- 產出目標：2 份 system design 文件、1 篇 security writeup、解題 pattern 速查卡。
- **怎麼知道有沒有效？** 第 2 月底：NeetCode 75 完成，30 分鐘內能草圖任何基礎系統。

---

**Phase 2 — Depth（第 3–5 月）**
*加入 OS / Network / Distributed / DB 輪流支線。交付第一批真正的程式碼成果。*

- 解題練習：維持每天 3–5 題。重心轉移到 hard 題和 pattern 組合。
- System Design：進入分散式系統設計。寫完整 design doc，含 failure mode 分析。
- 輪流支線：第 3 月 → OS + Network，第 4 月 → Distributed Systems，第 5 月 → Database Internals。
- 每月產出目標：1 個可運作的實作（HTTP server → Raft → KV store）。
- **怎麼知道有沒有效？** 第 5 月底：Raft 實作完成，KV store 存在，能深入討論 OS scheduler 和 LSM-tree。

---

**Phase 3 — Differentiation（第 6–8 月）**
*交付 senior level 產出。啟動 AI/LLM track。發布開源 security 作品。*

- 解題練習：維持每天 2–3 題。質量優於數量 — 專注 hard 題和模擬面試條件。
- System Design：寫 3 份 senior level 完整文件（geo-distributed、ML platform、real-time pipeline）。
- Security：發布開源 attestation library。SPIFFE/SPIRE 整合。提交 talk abstract。
- AI/LLM：在現有平台上建 RAG pipeline。vLLM benchmark 報告。Secure inference 架構文件。
- **怎麼知道有沒有效？** 第 8 月底：能設計帶 failure mode 分析的分散式系統，有 2 個開源專案，有 1 篇技術文章公開發布。

---

**Phase 4 — Interview Sprint（第 9–10 月）**
*所有事情都面向面試。從學習轉為在壓力下執行。*

- 解題練習：每天 3 題，計時，不看提示。回顧前幾個月每一道 hard 題。
- System Design：只做 mock interview。每週 3 次，錄影自我檢討。
- Behavioral：5 則 STAR 故事定稿。涵蓋：leadership、conflict、ambiguity、failure、impact。
- Portfolio：整理 `OUTPUTS/README.md` 成 portfolio 頁面。履歷最終版。
- **怎麼知道有沒有效？** 第 10 月底：任何 Google 面試格式都能從容應對，產出本身會說話。

---

## 調整規則

> 明確的 if-then，不是模糊建議。遇到狀況時直接查這裡。

**降載：** sustainability 評分連續兩週 ≤ 2 → 預設切換 Minimum Day 兩週。暫停輪流支線，只維持 DSA + 一個差異化方向。

**切換主技能：** 某支線連續三週 session 次數為零 → 停放它，從 `NOW/queue.md` 拉入下一條。不要強迫沒有發生的進度。

**暫停 track：** 工作突然爆量超過兩週 → 明確停放所有支線。只維持主線三條（DSA + System Design + Security）。在 `NOW/focus.md` 記錄暫停原因與預計恢復時間。

**切換成產出模式：** 如果連續三週以上都是消費（讀書、看影片、解題）卻沒有產出 → 宣告「產出週」。不學新東西，只 build、write、code。從 `NOW/queue.md` 的 output queue 拉清單。

**增加 mock interview：** 第 8 月起，如果還沒開始做 mock → 強制每週至少 1 場。不舒適感就是有效的訊號。

**新機會出現：** 對照十個月目標評估。如果直接相關（例如有機會發表、演講、或交付 security/AI 相關作品）→ 做，停放一條支線。如果無關 → 放進 `NOW/queue.md`，第 10 月後再做。

---

## 解題訓練策略

**目標：建立 pattern 識別能力，而非背解法。來源不限 LeetCode，書本題目同等有效。**

**做法：**
1. 依 pattern 分類，而不是依難度或平台（Two Pointers、Sliding Window、BFS/DFS、DP 等）
2. 每題記錄：來源、章節或題號、花費時間、解題思路、錯誤點、核心洞察
3. 沒解出或超時的題目，一週後盲解（不看自己的筆記）
4. 在 `LEETCODE/patterns/` 維護 pattern 速查卡，書本題目同樣以 pattern 歸類

```
LEETCODE/
├── log/
│   └── YYYY-MM-DD.md          # 每日解題日誌（來源可以是 LeetCode 或書本）
├── patterns/
│   ├── sliding-window.md
│   ├── two-pointers.md
│   ├── dynamic-programming.md
│   └── ...
└── strategy.md
```

**每週目標：** 5–7 題，深度研讀 1 個 pattern。

### 初始 10 題（啟動用，LeetCode 或書本皆可）

| # | 題目 | Pattern | 難度 | 狀態 |
|---|---|---|---|---|
| 1 | Two Sum | Hash Map | Easy | ⬜ |
| 2 | Valid Parentheses | Stack | Easy | ⬜ |
| 3 | Merge Two Sorted Lists | Linked List | Easy | ⬜ |
| 4 | Best Time to Buy and Sell Stock | Sliding Window | Easy | ⬜ |
| 5 | Maximum Subarray | Kadane's / DP | Medium | ⬜ |
| 6 | Number of Islands | BFS/DFS | Medium | ⬜ |
| 7 | Coin Change | DP | Medium | ⬜ |
| 8 | Longest Substring Without Repeating Characters | Sliding Window | Medium | ⬜ |
| 9 | Binary Search | Binary Search | Easy | ⬜ |
| 10 | Climbing Stairs | DP | Easy | ⬜ |

---

## 閱讀系統

**書單管理：**
- 優先序書單放在 `READING/booklist.md`
- 每本書一份筆記，放在 `READING/notes/`

**每本書的筆記格式：**
- 核心論點
- 關鍵概念（加上自己的詮釋）
- 可執行的行動
- 值得保留的引用

**複習節奏：**
- 每章讀完：趁記憶新鮮立刻記錄
- 讀完整本：在 `READING/summaries/` 寫一頁書摘
- 每月：重讀最近讀完的書的書摘

### 初始書單

| 書名 | 分類 | 狀態 |
|---|---|---|
| 內行人才知道的系統設計面試指南 | 系統設計 | 🔵 進行中 |
| 多模態生成式 Agent 實現（技術文件 + 論文） | AI / Agent | 🔵 進行中 |

---

## 技術筆記系統

技術筆記放在 `NOTES/`，依領域分類。每篇筆記要求：

- **原子性** — 一個概念，一份檔案
- **自完備** — 不需要其他筆記的前置知識即可閱讀
- **有連結** — 引用相關筆記的檔名
- **有日期** — 時效性內容用 `YYYY-MM-DD-topic.md` 命名

筆記不是正式文件。它是工作知識——需要粗糙的地方就粗糙，需要精確的地方要精確。

---

## 默寫系統

`MEMORIZATION/` 放的是需要主動回憶、而非被動閱讀的內容。

**適用內容：**
- 演算法複雜度速查表
- 系統設計元件特性
- 資安攻防分類法
- CLI 指令、API 模式、協定細節

**格式：** `MEMORIZATION/daily/` 裡每份檔案是一組 Q&A 或填空題，5–10 分鐘可複習完畢。

**選配：** 可匯出至 Anki 或 Obsidian 做間隔重複。

---

## 進度追蹤

`PROGRESS/dashboard.md` 是系統當前狀態的唯一真相來源。

追蹤內容：
- 進行中的技術軌道與當前深度
- LeetCode 累計題數、每週平均、題型覆蓋率
- 書單完成 vs 進行中
- 習慣一致性（每日打卡數據）
- 每月亮點

`PROGRESS/habits.md` 記錄每日打卡：今天完成了哪些例行項目。

每週回顧時更新 dashboard。

---

## 每週 / 每月回顧

### 每週回顧（`REVIEWS/weekly/YYYY-WXX.md`）

每週必答：
1. 這週做了什麼？
2. 各個進行中的技術軌道有什麼進展？
3. 哪裡沒有達成計畫？
4. 下週最重要的一件事是什麼？
5. 有沒有值得保留的洞察？

### 每月回顧（`REVIEWS/monthly/YYYY-MM.md`）

1. 這個月達成了哪些里程碑？
2. 每日習慣的一致性如何？（用 PROGRESS/ 的數據）
3. 哪些技術軌道需要加強或減少投入？
4. 主計畫是否仍然與目標對齊？
5. 應該開始做什麼、停止做什麼、繼續做什麼？

---

## 2026 年 4 月目標

### 目標一：TPM / TCG Device Identity & Attestation 實現

**背景：** 擔任 TPM 專案的 TPM，目標是符合 TCG 標準，在嵌入式裝置上實現完整的 device identity 與 attestation 流程。

**具體目標：**
- [ ] 梳理 TCG 相關規範（TPM 2.0 spec、EK/AK 架構）
- [ ] 完成 device identity 的 key hierarchy 設計（EK → AK → DevID）
- [ ] 實現 attestation flow（quote + verification）
- [ ] 撰寫技術文件，能向 stakeholder 說明整體架構

**筆記位置：** `NOTES/security/tpm-tcg-device-identity.md`

---

### 目標二：CRA Survey — EU Cyber Resilience Act × MX93 安全架構

**背景：** 歐盟 CRA（Cyber Resilience Act）對 IoT 裝置的資安要求越來越嚴格，NXP MX93 本身具備 EdgeLock Secure Enclave + Secure Boot，可支援 hardware-backed device identity。目標是梳理 CRA 合規路徑，並設計一套可交付給 end user 使用的 onboarding 架構。

**技術架構核心：**
```
MX93
└── EdgeLock Secure Enclave
    ├── Secure Boot（firmware integrity）
    ├── Hardware-backed Device Identity（硬體根金鑰）
    └── PKI Integration
        ├── Secure Onboarding（製造 → 部署 → end user）
        └── Signed OTA（軟體更新完整性驗證）

CRA 合規覆蓋：
├── Article 10: Cybersecurity requirements by design
├── Vulnerability handling & security updates (Signed OTA)
└── Device identity & authentication requirements
```

**具體目標：**
- [ ] 完成 CRA 條文 survey，整理 IoT 相關要求對照表
- [ ] 輸出 MX93 EdgeLock + PKI 架構設計文件
- [ ] 設計 end user onboarding flow（含 provisioning、credential delivery）
- [ ] 評估 Signed OTA 的實作方案（如 SWUpdate + dm-verity）
- [ ] 整理成可對外說明的架構概述（含 compliance mapping）

**筆記位置：** `NOTES/security/cra-mx93-device-identity.md`

---

## 554 每日計畫

> **554 = 早上 5 小時 + 下午 5 小時 + 晚上 4 小時**
> 核心理念：早上是自己的，下午是工作的，晚上是深度的。

### 早上：自我建設（5 小時）

| 時段 | 時間 | 內容 |
|---|---|---|
| 核心運動 | 06:00 – 06:30 | 核心訓練（棒式、捲腹、功能性動作） |
| 有氧 + 英文 | 06:30 – 07:30 | 跑步機 1 小時，同步聽英文（Podcast / TED / 技術演講），強化英文輸入 |
| 重訓 | 07:30 – 08:00 | 重量訓練 |
| *(緩衝 / 梳洗)* | *08:00 – 08:30* | *準備 / 換狀態* |
| 默寫 | 08:30 – 09:00 | 默寫前一天的學習筆記，不看書，直接輸出 |
| LeetCode | 09:00 – 11:00 | 刷題 2 小時（解題 + 記錄 + 複習錯題） |
| 英文口說 | 11:00 – 12:00 | 英文口說練習（shadowing / 自言自語 / iTalki / AI 對話） |
| 面試準備 | 12:00 – 12:30 | 模擬回答、整理 STAR 故事、或複習系統設計題 |

**早上合計：5 小時**

---

### 下午：工作專業（5 小時）

| 時段 | 時間 | 內容 |
|---|---|---|
| 工作 | 13:30 – 18:30 | 工作專業發展（TPM 項目、CRA、技術實作） |

> 工作時間也是成長時間。TPM 項目的推進直接對應 4 月目標。

---

### 晚上：深度建設（4 小時）

| 時段 | 時間 | 內容 |
|---|---|---|
| 系統設計書單 | 19:30 – 21:00 | 閱讀《內行人才知道的系統設計面試指南》或多模態 Agent 文件 |
| 稀缺專長 | 21:00 – 22:30 | 深度稀缺專長建立（TPM/TCG、CRA、硬體安全、AI Agent 實現） |
| 收尾歸納 | 22:30 – 23:30 | 整理當天所有學習，寫入筆記系統，準備明天的默寫內容 |

**晚上合計：4 小時**

---

### 每週習慣打卡欄位（`PROGRESS/habits.md` 使用）

| 習慣 | M | T | W | T | F | S | S |
|---|---|---|---|---|---|---|---|
| 核心運動 | | | | | | | |
| 跑步 + 英文 | | | | | | | |
| 重訓 | | | | | | | |
| 默寫 | | | | | | | |
| LeetCode | | | | | | | |
| 英文口說 | | | | | | | |
| 面試準備 | | | | | | | |
| 系統設計閱讀 | | | | | | | |
| 稀缺專長 | | | | | | | |
| 收尾筆記 | | | | | | | |

---

## 履歷

履歷文件放在 `RESUME/`，版本管理，隨時可輸出。

```
RESUME/
├── resume-zh.md          # 中文履歷
├── resume-en.md          # 英文履歷
├── resume-zh.pdf         # 輸出用 PDF（不 commit 草稿）
└── resume-en.pdf
```

---

## 開始使用

```bash
git clone https://github.com/YOUR_USERNAME/tzc-engineering-growth-system.git
cd tzc-engineering-growth-system

# 每天的入口
open today.md

# 查看現在哪些 track 是 active
open now/focus.md

# 建立今天的 log
touch logs/$(date +%Y-%m-%d).md

# 本週回顧（複製 template）
cp reviews/weekly/template.md reviews/weekly/$(date +%G-W%V).md
```

每天打開 `today.md`，宣告今天是哪種模式（Minimum / Normal / Deep），填三個欄位，完成三個 checkbox。或者直接用 `/daily-repo-operator` 讓 Claude 幫你完成整個流程。

---

## 每日操作流程

### 使用 Claude 自動完成（建議）

這個 repo 有一個 custom skill：`.claude/commands/daily-repo-operator.md`。

每天分兩段：早上 Claude 幫你建立今天的檔案、開好 inbox；白天你只需要把東西寫進 `inbox/`；晚上 Claude 讀 inbox 並自動分類整理。

---

### 三個檔案，三個角色

| 檔案 | 用途 | 誰來寫 |
|---|---|---|
| `inbox/YYYY-MM-DD.md` | 白天原始材料入口，不需整理 | 你（白天隨時寫） |
| `logs/YYYY-MM-DD.md` | 正式執行紀錄，結構化、有 checkbox | Claude（早上 + 晚上） |
| `today.md` | 當天操作面板，永遠與 log 同步 | Claude（每次更新 log 後覆寫） |

**白天只要顧 inbox。晚上讓 Claude 整理。**

---

### 開始今天

對 Claude 說：

> 「開始今天」、「幫我開始今天」、「今天 Normal day，要做 X」

Claude 會：
1. 建立 `inbox/YYYY-MM-DD.md`（空白模板，等你白天填）
2. 建立 `logs/YYYY-MM-DD.md`（填入模式、解題、主技能、micro-goal、預期產出）
3. 同步覆寫 `today.md`
4. 執行 `git commit -m "daily: YYYY-MM-DD start (plan)"` 並 push

如果你沒說清楚今天要做什麼，Claude 只問一個問題：「今天主要做什麼？」

---

### 白天：只寫 inbox

打開 `inbox/YYYY-MM-DD.md`，想到什麼就寫在對應區塊：

- 解題思路 / 書本題記錄
- 技術思考、架構想法、程式碼片段
- 想記住的知識點
- 卡住的地方
- 明天下一步

**不用管格式，不用管分類，晚上 Claude 會處理。**

---

### 今天結束

對 Claude 說：

> 「今天結束」、「今天做完了」、「幫我收尾今天」、「收工」

Claude 會：
1. 讀 `inbox/YYYY-MM-DD.md`，自動分類到正確位置：
   - 解題記錄 → `leetcode/log/YYYY-MM-DD.md`
   - 技術筆記 → `notes/security/`、`notes/systems/`、`notes/misc/` 等（依關鍵字路由）
   - 適合背誦的內容 → `memorization/daily/YYYY-MM-DD.md`
2. 更新 `logs/YYYY-MM-DD.md`：填「做了什麼」、「卡住的地方」、打勾完成條件
3. 若有實質進展，更新 `progress/dashboard.md`
4. 同步覆寫 `today.md`
5. 執行 `git commit -m "daily: YYYY-MM-DD progress (<summary>)"` 並 push

**inbox 原始材料永遠保留，不刪不改。**

---

### 範例：開始今天

```
今天 Normal day。我要做 C++ 解題入門第 1 章 1-1 ~ 1-3，
然後做 TPM agent SRK redesign，目標是把 persistent handle 全部移掉。
```

Claude 建立：
- `inbox/YYYY-MM-DD.md`（空白模板）
- `logs/YYYY-MM-DD.md`：模式 Normal、書本第 1 章、主技能 05-security、micro-goal：移除 persistent handle
- `today.md`（鏡像 log）
- commit: `daily: YYYY-MM-DD start (plan)`

---

### 範例：今天結束

```
今天收工。書本 1-1 ~ 1-3 都解完了，獨立解出。
TPM key hierarchy 梳理完了，AK 要 persistent，DevID 可以 transient。
寫了一份 SRK redesign 筆記。
```

Claude 執行：
- inbox 內容 → 建立 `notes/security/YYYY-MM-DD-tpm-agent-srk-redesign.md`
- 解題記錄 → `leetcode/log/YYYY-MM-DD.md`
- 更新 `logs/YYYY-MM-DD.md`，打勾完成條件
- commit: `daily: YYYY-MM-DD progress (TPM SRK key hierarchy, C++ ch1)`

---

### Commit 規則

| 時機 | 格式 |
|---|---|
| 開始今天 | `daily: YYYY-MM-DD start (plan)` |
| 收尾 / 更新進度 | `daily: YYYY-MM-DD progress (<summary>)` |

`summary` 用英文，不超過 50 字，描述今天實際做了什麼。

---

### 原則

- 白天先寫 inbox，不急著分類
- 晚上再由 Claude 整理，不要手動移動 inbox 內容
- `inbox/` 保留原始材料，永不刪除
- `logs/` 是正式執行紀錄，不刪不改只追加
- `today.md` 是當天面板，永遠與當天 log 同步
- 每天至少兩次 commit：開始一次（plan），收尾一次（progress）
- 當日 log 的 commit 不混入其他系統變更

---

## 使用規則

**每日（必做）：**
- 填寫 `TODAY.md`，三個 checkbox 全打勾才算完成
- 更新 `PROGRESS/habits.md` 今日打卡
- 把任何產出歸檔到 `NOTES/` 或 `OUTPUTS/`

**每週（必做，週日）：**
- 完成每週回顧 → `REVIEWS/weekly/YYYY-WXX.md`（複製 template）
- 更新 `PROGRESS/dashboard.md`
- 填寫下週的 `THIS_WEEK.md`

**每月（必做）：**
- 完成每月回顧 → `REVIEWS/monthly/YYYY-MM.md`（複製 template）
- 更新 `NOW/focus.md` — 調整 active track，從 `NOW/queue.md` 輪入新支線
- 更新 `PROGRESS/dashboard.md` 月度欄位

**一般原則：**
- 系統感覺太重 → 簡化它，不要硬撐。可持續運作才是目標
- 跳過回顧 = 在沒有 feedback loop 的情況下繼續 — 這比進度落後更危險
- 筆記是寫給自己的，清楚即可，不必過度打磨
- 小而一致的 commit 優於大批次

---

*最後更新：2026-04-02*
