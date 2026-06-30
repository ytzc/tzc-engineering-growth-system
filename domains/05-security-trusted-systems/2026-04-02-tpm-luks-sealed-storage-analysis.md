# TPM + LUKS / Sealed Storage 架構分析 — 2026-04-02

---

## 一、目前系統架構（現況理解）

### tree create 流程

```
tree-cli
  → handle_command::create
    → 確認 tpm_api_server
  → TreeController::create_tree  ⭐核心
    → sealed_storage_handler::allocate_sealed_storage
      → run_secure_storage_client
        → SSS::LocalCreateEncryptedVolume
    → sealed_storage_handler::sync_data_to_sealed_storage
      → RsyncClient
    → container_controller::create
      → docker compose up
```

---

## 二、Sealed Storage（SSS）流程

### Volume 建立流程

1. 建立 LVM
2. TPM Agent → InitializeLuksKeySlot（取得初始 secret）
3. cryptsetup luksFormat（用 secret 當 key）
4. cryptsetup luksOpen
5. mkfs.ext4
6. mount
7. rsync（可選）
8. umount + luksClose

### Key 管理流程

9. TPM Agent → generate_pcr_bound_key
10. cryptsetup luksAddKey（加入 TPM PCR key）
11. rm init_key_tmp

---

## 三、Runtime 解密流程（Kata）

```
kata-runtime
  → tpm-agent-cli
    → unseal-pod-handle
    → pcr-reset-extend
  → 解出 LUKS passphrase
```

---

## 四、已確認問題

### P0（必須優先）

**問題 1：TPM handle 使用方式（重大）**
- 每個 volume / pod 使用 persistent handle ❌
- TPM handle 數量有限（不 scalable）
- 尚未釐清：handle allocation 策略、是否需要 per-pod handle

**問題 2：Key lifecycle 不完整**
- 沒有 rotate / revoke
- 沒有 version control
- 尚未釐清：LUKS key slot 使用策略、TPM key vs volume key 關係

**問題 3：create vs run 邊界不清楚**
- create 時就生成 TPM key
- run 時才真正使用
- 尚未釐清：attestation 發生在哪？trust boundary 在 host 還是 guest？

### P1（架構問題）

**問題 4：sealed-storage 與 container 綁定**
- 目前：pod_id → volume → TPM key
- 尚未釐清：identity 是否應來自 attestation？是否需要 workload identity？

**問題 5：資料同步流程分離**
- create → 建空 volume，再 rsync → 可能 partial failure，非 atomic

**問題 6：GPU PCIe 問題** — 暫緩（非核心）

---

## 五、關鍵設計轉向

### 分兩層設計

**Layer 1：Storage（標準化）**
- systemd-cryptenroll / systemd-cryptsetup
- 解決：LUKS + TPM 綁定、key slot 管理、unlock 流程

**Layer 2：Identity（核心目標）**
- attestation（Kata / TEE）
- policy（KBS / Trustee）
- workload identity
- 控制：誰可以拿到 LUKS key

### 重要結論

> **TPM + LUKS ≠ sandbox identity**
>
> sandbox identity 應該來自 attestation + guest measurement

---

## 六、尚未釐清的核心問題

**問題 A：TPM 正確使用模型**
- 現在：TPM → 直接產 LUKS key ❌
- 應該：TPM (SRK) → KEK（少量）→ LUKS volume key（大量）

**問題 B：systemd-cryptenroll 是否取代現有流程？**
- [ ] 完全改用 systemd？
- [ ] 還是維持自建 + TPM agent？

**問題 C：Kata identity 怎麼綁 key？**
- 用 PCR？attestation？KBS？

**問題 D：key 存在哪？**
- TPM NV？LUKS slot？外部 KMS？

---

## 七、明天行動計畫

| Task | 內容 |
|---|---|
| T1 | 設計正確 key hierarchy：TPM → KEK → volume key 設計圖 |
| T2 | 比較 TPM agent 自建 vs systemd-cryptenroll，畫流程差異圖 |
| T3 | 設計 sandbox identity flow（attestation / KBS / Trustee） |
| T4 | 修正 TPM handle 使用：改成少量 persistent key 或 transient key |
| T5 | tpm-agent README、單元測試、sealed-storage API 整理（次要） |

---

## 一句話總結

> 目前設計 = 「TPM 驅動 storage」
> 正確方向 = 「TPM + attestation 驅動 identity，storage 只是載體」
