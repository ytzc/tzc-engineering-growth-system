# LeetCode 策略

## 核心原則

**目標是題型識別，不是背解法。**

看到一道題，腦中要能立刻問：「這是什麼結構？適合哪種模式？」
這個能力是刷出來的，不是看解答看出來的。

---

## 每題記錄格式

```markdown
## [題號] 題目名稱

- **難度：** Easy / Medium / Hard
- **題型：** Sliding Window / DP / BFS / ...
- **花費時間：** XX 分鐘
- **狀態：** AC / WA / TLE / 看提示

### 解題思路
（用自己的話描述，不要複製貼上）

### 關鍵洞察
（這題最重要的一個觀察是什麼）

### 錯誤 / 陷阱
（自己踩到的坑，或常見錯誤）

### 時間 / 空間複雜度
- Time: O(?)
- Space: O(?)
```

---

## 每週目標

- **題數：** 5–7 題
- **題型深讀：** 每週選 1 個題型，深度理解並更新 `patterns/`
- **複習：** 上週錯題 / 慢題，重新解一遍

---

## 初始 10 題（啟動清單）

| # | 題目 | 類型 | 難度 | 狀態 | 日期 |
|---|---|---|---|---|---|
| LC1 | Two Sum | Hash Map | Easy | ⬜ | |
| LC20 | Valid Parentheses | Stack | Easy | ⬜ | |
| LC21 | Merge Two Sorted Lists | Linked List | Easy | ⬜ | |
| LC121 | Best Time to Buy and Sell Stock | Sliding Window | Easy | ⬜ | |
| LC53 | Maximum Subarray | Kadane's / DP | Medium | ⬜ | |
| LC200 | Number of Islands | BFS/DFS | Medium | ⬜ | |
| LC322 | Coin Change | DP | Medium | ⬜ | |
| LC3 | Longest Substring Without Repeating Chars | Sliding Window | Medium | ⬜ | |
| LC704 | Binary Search | Binary Search | Easy | ⬜ | |
| LC70 | Climbing Stairs | DP | Easy | ⬜ | |

---

## 題型索引

| 題型 | 說明檔 | 常見題 |
|---|---|---|
| Sliding Window | `patterns/sliding-window.md` | LC3, LC121, LC209 |
| Two Pointers | `patterns/two-pointers.md` | LC167, LC15, LC11 |
| BFS / DFS | `patterns/bfs-dfs.md` | LC200, LC102, LC133 |
| Dynamic Programming | `patterns/dynamic-programming.md` | LC70, LC322, LC53 |
| Binary Search | `patterns/binary-search.md` | LC704, LC33, LC153 |
| Hash Map | `patterns/hash-map.md` | LC1, LC49, LC128 |
| Stack | `patterns/stack.md` | LC20, LC42, LC84 |
| Linked List | `patterns/linked-list.md` | LC21, LC206, LC141 |
