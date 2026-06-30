# 3 年技術成就總結與能力展望 (Portfolio Summary)

> **楊子擎 (Jerry Yang) · 邊信聯科技 (FiduciaEdge Technologies) 軟體工程師**
> *深耕於硬體安全信任根、機密邊緣運算、可信物聯網設備安全與自動化代碼簽章沙盒系統。*

---

## 一、核心技術實力與知識版圖 (Core Capabilities)

在邊信聯科技 (FiduciaEdge) 的三年研發工作中，我專注於「硬體安全防護」與「雲端/邊緣運算平台」的交會處。我的核心能力跨越了從硬體晶片層、作業系統核心層，到雲端容器化部署的完整信任鏈 (Chain of Trust) 構建。

### 1. TPM 2.0 硬體安全與設備憑證佈署 (Hardware Security Root of Trust)
- **設備唯一識別 (IDevID / LDevID)**：精通基於 IEEE 802.1AR 標準的設備身分識別。設計多種在生產端與設備端安全佈署 IDevID 的機制。
- **金鑰複製與遷移策略**：深度掌握 `TPM2_Duplicate`、`TPM2_Import`、`TPM2_Load` 命令與相關複製策略（Policy）。實現將伺服器端（或 CA 端）生成的 IDevID 以 EK 公鑰加密保護（Parent Key 為 EK），安全傳輸並導入至目標客戶端設備的 TPM 晶片中，確保私鑰在傳輸與落地過程中不落地且不可被竊取。
- **金鑰層級結構 (Key Hierarchy)**：精通 TPM 2.0 內置的 SRK (Storage Root Key)、EK (Endorsement Key)、AIK/AK (Attestation Key) 的責任與資料流，實現高安全性與高擴展性的金鑰架構。

### 2. 作業系統硬體安全架構與安全啟動 (System & Platform Security)
- **Nvidia Jetson Tegra 安全防護**：掌握 Jetson Nano / TX2 / Xavier 的安全啟動流程。研讀 Tegra Linux Driver Package (L4T) 開發指南，專注於硬體保險絲（Fuses）燒錄、安全金鑰寫入與 Bootloader 簽章流程。
- **UEFI Secure Boot & Measured Boot**：實現基於 MOK (Machine Owner Key) 的 Linux 核心模組與驅動程式簽章。建置 UEFI Measured Boot 機制，將啟動各階段（Firmware、Bootloader、Kernel）的 Hash 值度量（Measure）寫入 TPM 的 PCR (Platform Configuration Register) 中，做為遠程驗證的身分憑證。

### 3. 可信容器運算平台與 TEE 沙盒 (Confidential Edge Computing)
- **fECP 可信容器化平台**：參與研發基於 Kubernetes/AWS 的可信容器部署架構 (fECP v1.5)，實現雙向 MTLS 安全通訊與安全的邊緣 OTA 更新。
- **cosnar 容器驗證與 TEE 隔離**：開發 `cosnar` 機制，在設備運行時即時驗證容器來源及完整性。在設備端建構隔離應用程式與硬體的 TEE-REE 執行環境（CCSars），確保敏感計算資料無法被外部硬體或權限妥協的 Host 作業系統存取。

### 4. 企業級自動代碼簽章沙盒系統 (Enterprise Code Signing Sandbox)
- **TWCA 憑證認證與整合**：精通與台灣網路認證公司 (TWCA) API 整合。設計自動化申請與下載 X.509 公鑰證書、建置 PKCS12 (PFX) 金鑰管理機制。
- **代碼簽章服務主機 (Sign Daemon)**：主導設計高安全性的 Code Signing 沙盒流程，分為 **Hash Sandbox (哈希沙盒)**、**Sign Sandbox (簽章守護進程)** 與 **Verify Sandbox (驗證沙盒)**。
  - 設計高性能的 `hashtool.jar` 進行代碼/韌體度量雜湊（SHA256）。
  - 開發 `signtool.jar` 做為背景 Daemon，串接 TWCA 加密模組，支持 RSA 簽章（P1 格式與 P1_WITH_HASHED 格式）。
  - 封裝為標準的 P7 (PKCS7/CMS) 憑證附加與代碼雜湊綁定結構，確保韌體從發布到執行（E2E File Transfer）的完整性、真實性與不可否認性（Non-repudiation）。

---

## 二、主導之關鍵專案與實質貢獻 (Key Projects & Impact)

### 1. Trusted Things 可信物聯網設備解決方案 (矽到雲安全)
- **角色**：核心軟體研發工程師
- **貢獻**：設計並編寫信任鏈概念驗證與序列圖 (Sequence Diagram)。引入 TPM 2.0 硬體晶片作為物理信任根，實現設備啟動時即時度量 UEFI/驅動程式/CCSars 韌體，並在邊緣端透過 mTLS 構建加密加密通道。成功解決傳統 IoT 設備身分易被仿冒、邊緣運算資料易在傳輸時遭攔截的痛點。

### 2. 邊端代碼/韌體簽章自動化測試與發布系統 (A3 交易模組)
- **角色**：架構設計與整合開發者
- **貢獻**：將 TWCA 憑證認證、私鑰防護與 PE/ELF 代碼簽章深度融合。設計拆分了 **A3.1 安裝操作說明書、容器化部署說明書、可信運算說明書**等關鍵技術文件。編寫測試驗證程序，全方位確保邊端交易在極端受攻擊環境下的「機密性、完整性、真實性與不可否認性」，並成功通過外部安全合規性驗證。

### 3. fECP/CCSars 邊緣安全沙盒
- **角色**：核心維護與優化工程師
- **貢獻**：維護 fECP v1.5 (K8s) 環境下的安全沙盒，編寫系統升級更新腳本 (Update Script)，透過 Sandbox 對網路上的虛擬主機 (vHub) 及邊端設備進行極低摩擦、高度安全驗證的熱更新與 OTA。

---

## 三、個人核心優勢與能力展望 (Professional Capacity Outlook)

作為一名在硬體安全與軟體工程交會點工作了三年的研發人員，我已建立起高度稀缺的**「軟硬一體化安全架構」**實戰優勢。

### 1. 我的稀缺競爭優勢 (My Differentiators)
- **懂雲原生、也懂硬體底層**：絕大多數 Security 工程師僅熟悉應用層安全、Web 滲透或 IAM 規則；而傳統硬體/韌體工程師往往忽略雲端分布式架構與容器安全。我能無縫串聯 **TPM 晶片/Trustzone → 核心核心模組簽章 → 容器完整性驗證 (cosnar) → 雲原生 Attestation 驗證** 的完整通路。
- **企業級 PKI 與硬體信任結合實戰**：擁有與台灣最權威證書機構 (TWCA) 整合的大型生產系統開發經驗，這在需要金融級安全、高階車聯網或軍民雙用安全系統開發中極具競爭力。

### 2. 未來技術演進與能力展望 (Future Roadmap)
- **從「硬體金鑰整合」演進到「大規模遠程驗證 (Remote Attestation at Scale)」**：
  - 目前我已精通 TPM 2.0 單機金鑰複製與本地度量驗證。下一步我將專注於深入標準化遠程驗證架構（如 **IETF RATS RFC 9334** 規範）。
  - 計畫建置基於 **SPIFFE/SPIRE** 的工作負載硬體驗證 (Workload Attestation) 系統，將物理設備 TPM 的證明信息無縫轉化為雲端微服務的動態身分證（SVID），將邊端安全真正對齊雲原生架構。
- **向主流大廠「機密運算 (Confidential Computing)」架構對齊**：
  - 將技術廣度由 ARM TrustZone / 專屬 TEE，拓寬至當前雲端主流硬體安全防護：如 **Intel TDX**、**AMD SEV-SNP** 與 **ARM CCA**。
  - 深入研究可信密鑰管理服務 (KBS / KMS) 與 Remote Attestation (如 Keylime 專案) 的整合，使我在高階安全工程師或資深資安架構師的角色中具備全球領先的競爭力。
