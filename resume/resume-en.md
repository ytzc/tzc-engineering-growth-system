# Tz-Ching Yang

**AI Infrastructure & Trusted Systems Engineering**

ytz1298@gmail.com · (+886) 966-765-256

---

## Summary

Systems engineer specializing in hardware-rooted security and on-premises AI infrastructure. Four years building production platforms where trust is cryptographically enforced rather than assumed — spanning TPM-based IoT provisioning (1,000+ managed endpoints, zero manual intervention) and private LLM inference with hardware-level tenant isolation. Owns end-to-end architecture from hardware security elements to application APIs. Holds an international patent on privacy-preserving device attestation (PCT/IB2023/063389).

---

## Experience

### FiduciaEdge Technologies · Technical Lead, AI Infrastructure & Security Systems
*2021 – Present*

**Trusted Things Provision Service** — *Zero-Touch IoT Security Provisioning Platform*

Designed and delivered an automated device onboarding system that manages 1,000+ endpoints without human intervention. Each device receives a unique cryptographic identity at boot; no static credentials exist on any device.

- Architected an identity pipeline using TPM 2.0 and FIDO FDO, eliminating credential-leakage risks endemic to manual IoT provisioning at scale.
- Built multi-tenant workload isolation on lightweight Kubernetes (k3s), enabling multiple independent services to share edge hardware securely without cross-tenant interference.
- Invented a privacy-preserving device attestation scheme allowing devices to prove integrity without revealing identity; filed as international patent **PCT/IB2023/063389**.

**Trusted On-Premise GenAI Server** — *Private AI Inference Platform*

Designed and delivered a self-hosted LLM inference platform for organizations with compliance or confidentiality constraints that prevent public-cloud AI use.

- Built a secure inference stack that protects model weights at rest and verifies model integrity before each startup, preventing model tampering or substitution.
- Achieved near-bare-metal GPU performance across isolated multi-tenant workloads via hardware-level GPU partitioning (**<5% overhead**), making private AI deployment commercially viable without per-tenant hardware.
- Bound service startup to hardware remote attestation, ensuring the AI server executes only on policy-validated nodes — establishing a hardware-rooted trust anchor for the entire inference environment.

---

## Education

**National Chiao Tung University (NCTU)** · M.S., Computer Science · 2018 – 2020
Thesis advisor: Prof. Tien-Fu Chen

**National Chengchi University (NCCU)** · B.S., Computer Science · 2013 – 2017

---

## Skills

| Domain | Details |
|---|---|
| **Trusted Systems** | TPM 2.0, FIDO FDO/DICE, Remote Attestation, Secure Boot, TEE |
| **AI Infrastructure** | On-prem LLM deployment, GPU resource isolation, model lifecycle security |
| **Platform Engineering** | Kubernetes / k3s, multi-tenant isolation, GPU-aware workload scheduling |
| **Security** | PKI / X.509 automation, zero-trust architecture, hardware attestation |
| **Languages** | Rust · Python · C/C++ |
| **Patents** | PCT/IB2023/063389 — Privacy-Preserving Device Attestation |
