# 今天 — 2026-04-02

**今天的模式：** `[ ] Minimum` `[x] Normal` `[ ] Deep`

---

## 解題練習 — 每天必做

- **來源：** `[ ] LeetCode` `[x] 書本` `[ ] 其他`
- **題目 ID / 章節：** 第 1 章 1-1 ~ 1-3
- **題目名稱：** 輸入輸出與基本技巧
- **Pattern：** Basic I/O / Simulation
- **花費時間：** ___
- **結果：** `[ ] 獨立解出` `[ ] 看提示後解出` `[ ] 看解答理解`
- **核心洞察（一句話）：** ___

---

## 主技能 — Track 05 Security & Trusted Systems

**Track：** `SKILLS/05-security-trusted-systems/`

**今天的微目標（一句話）：** 把 tpm-agent 的 persistent handle 拿掉，改成 SRK-based

**做了什麼：**
- 梳理 tpm-agent 現有架構：tree create → SSS → TPM → LUKS 完整流程
- 確認 P0 問題：per-volume persistent handle 不 scalable、key lifecycle 不完整、create/run 邊界不清
- 識別 P1 問題：sealed-storage 與 container 綁定靠 pod_id、rsync 非 atomic
- 發現關鍵設計轉向：應分 Storage（systemd-cryptenroll）與 Identity（attestation + KBS）兩層
- 核心洞察：TPM + LUKS ≠ sandbox identity；correct key hierarchy 應為 SRK → KEK → volume key

**卡住的地方：**
- systemd-cryptenroll 是否完全取代自建 TPM agent 流程，尚未決定
- Kata identity 如何綁 key（PCR / attestation / KBS）尚未釐清
- key 存放位置（TPM NV / LUKS slot / 外部 KMS）尚未決定

---

## 產出 — 一個小東西

- [x] TPM + LUKS sealed storage 架構分析筆記
  → `NOTES/security/2026-04-02-tpm-luks-sealed-storage-analysis.md`

---

## 完成條件

- [ ] 解題：1 題做完並記錄
- [x] 技能：focused session（deep analysis of tpm-agent architecture）
- [x] 產出：1 個東西歸檔

---

## 備註 / 阻礙

- 解題今天未完成，明天補上

---

*只能做一件事的話：做解題練習。*
*有兩小時：解題 + TPM 設計。*
*有四小時以上：補完整 key hierarchy architecture 筆記。*
