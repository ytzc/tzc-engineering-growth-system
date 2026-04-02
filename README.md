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
├── SKILLS/                      # 10 個技術學習軌道
│   ├── 01-data-structures-algorithms/
│   ├── 02-system-design/
│   ├── 03-backend-engineering/
│   ├── 04-databases/
│   ├── 05-security/
│   ├── 06-networking/
│   ├── 07-operating-systems/
│   ├── 08-distributed-systems/
│   ├── 09-devops-infrastructure/
│   └── 10-software-engineering-practices/
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

## 學習系統架構

系統分三個時間尺度運作：

**每日（15–60 分鐘）**
- LeetCode：解 1 題或複習 1 個題型
- 默寫：複習前一天的學習筆記
- 筆記：記錄當天任何有價值的洞察

**每週（1–2 小時，專屬時段）**
- 深度推進 1 個技術軌道
- 閱讀書單進度
- 撰寫每週回顧

**每月（2–4 小時）**
- 盤點 10 個技術軌道的缺口
- 更新里程碑與主計畫
- 撰寫每月回顧並看數據

---

## 10 個技術學習軌道

每個軌道放在 `SKILLS/XX-track-name/`，包含：
- `roadmap.md` — 這個技術的學習路徑與里程碑
- `notes/` — 結構化技術筆記
- `resources.md` — 精選資源、書籍、課程
- `log.md` — 每週進度記錄

| # | 軌道 | 狀態 |
|---|---|---|
| 01 | 資料結構與演算法 | 🔵 進行中 |
| 02 | 系統設計 | 🔵 進行中 |
| 03 | 後端工程 | 🔵 進行中 |
| 04 | 資料庫 | ⬜ 待啟動 |
| 05 | 資安 | ⬜ 待啟動 |
| 06 | 網路 | ⬜ 待啟動 |
| 07 | 作業系統 | ⬜ 待啟動 |
| 08 | 分散式系統 | ⬜ 待啟動 |
| 09 | DevOps 與基礎設施 | ⬜ 待啟動 |
| 10 | 軟體工程實踐 | ⬜ 待啟動 |

> 同時間只專注 2–3 個軌道，每月回顧時視需求輪換。

---

## LeetCode 策略

**目標：建立題型識別能力，而非背解法。**

**做法：**
1. 依題型分類（雙指針、滑動視窗、BFS/DFS、DP 等）
2. 每題記錄：難度、花費時間、解題思路、錯誤點、核心洞察
3. 錯題或超時題，一週後重解
4. 在 `LEETCODE/patterns/` 維護題型速查卡

```
LEETCODE/
├── log/
│   └── YYYY-MM-DD.md          # 每日刷題日誌
├── patterns/
│   ├── sliding-window.md
│   ├── two-pointers.md
│   ├── dynamic-programming.md
│   └── ...
└── strategy.md
```

**每週目標：** 5–7 題，深度研讀 1 個題型。

### 初始 10 題清單（啟動用）

| # | 題目 | 類型 | 難度 | 狀態 |
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

# 讀主計畫
open PLAN/master-plan.md

# 開啟今天的刷題日誌
touch LEETCODE/log/$(date +%Y-%m-%d).md

# 開啟本週回顧
touch REVIEWS/weekly/$(date +%G-W%V).md
```

從 `PLAN/master-plan.md` 開始。先定義你的 1 年目標、前三優先技術方向、每日承諾時間。其餘一切都從這裡展開。

---

## 使用規則

**每日（必做）：**
- [ ] 最少：打開一個檔案、新增一筆記錄、或解一道題
- [ ] 更新 `PROGRESS/habits.md` 今日打卡

**每週（必做）：**
- [ ] 完成每週回顧 `REVIEWS/weekly/`
- [ ] 更新 `PROGRESS/dashboard.md`
- [ ] 至少推進一個技術軌道

**每月（必做）：**
- [ ] 完成每月回顧 `REVIEWS/monthly/`
- [ ] 盤點技術軌道狀態，視需要輪換
- [ ] 更新 `PLAN/milestones.md`

**一般原則：**
- 沒有孤兒檔案——每個檔案都有歸屬
- 小而一致的 commit 優於大批次
- 筆記是寫給自己的，清楚即可，不必過度打磨
- 如果系統感覺太重，就簡化它——可持續運作才是目標

---

*最後更新：2026-04-02*
