# Track 05 · Security & Trusted Systems

> **Goal:** Be the definitive expert in hardware-rooted trust, attestation, and secure system architecture. This is your rarest and most differentiating capability — systematize and deepen it.

---

## Why It Matters

Security expertise at the hardware/firmware/OS intersection is genuinely rare. Most security engineers operate at the application layer; most systems engineers ignore security. You sit at the intersection: you build systems where trust is cryptographically provable, not assumed. This differentiates you not just in interviews but in the engineering market globally.

The Google Security team, Hardware Security team, and FIDO Alliance ecosystem all need people who understand what you have built.

---

## Core Knowledge

**Hardware Security Primitives**
- TPM 2.0 architecture: PCRs, EK/AK/IAK, key hierarchies, attestation key provisioning
- FIDO DICE (Device Identifier Composition Engine): layer-by-layer trust propagation
- FIDO FDO (FIDO Device Onboard): protocol phases, RV server, Owner Onboarding
- Secure boot chain: UEFI Secure Boot, measured boot, boot event log
- Hardware Security Modules (HSMs): PKCS#11, key ceremonies, FIPS 140-3

**Remote Attestation**
- TPM-based remote attestation: quote generation, quote verification, PCR policies
- RATS (Remote ATtestation procedureS) — IETF RFC 9334 architecture
- DICE-based attestation for constrained devices
- Confidential Computing: Intel TDX, AMD SEV-SNP, ARM CCA — TEE attestation
- Attested TLS — binding attestation evidence to TLS sessions

**PKI & Cryptographic Infrastructure**
- X.509 certificate chains, CRL, OCSP stapling
- EST (Enrollment over Secure Transport) and SCEP for automated PKI
- Certificate pinning vs. CA trust model
- Key derivation functions (HKDF, PBKDF2), KDF chaining in DICE
- Post-quantum readiness: CRYSTALS-Kyber, CRYSTALS-Dilithium basics

**Zero-Trust Architecture**
- Zero-trust network access (ZTNA) model
- Workload identity: SPIFFE/SPIRE, workload attestation
- Secret management: HashiCorp Vault, SOPS, envelope encryption
- Least-privilege enforcement: capabilities, seccomp, SELinux/AppArmor

**Supply Chain Security**
- SBOM (Software Bill of Materials): CycloneDX, SPDX
- Sigstore: Cosign, Rekor — artifact signing and transparency logs
- In-toto: software supply chain attestation framework
- SLSA (Supply chain Levels for Software Artifacts) framework

---

## How to Practice

1. **Extend your TPM work** — build an open-source attestation service that verifies TPM quotes against a reference PCR policy; publish it
2. **Implement DICE in software** — write a DICE layer emulator in Rust to understand the key derivation chain
3. **Set up a SPIRE cluster** — integrate SPIFFE workload identity into a k3s deployment
4. **Read the IETF RATS RFCs** — RFC 9334, RFC 8555 (ACME), RFC 7030 (EST)
5. **Write security advisories** — analyze a real CVE in an IoT/firmware product, document the root cause and mitigation
6. **Submit a talk abstract** — USENIX Security, CCS, or FIDO Alliance workshops

---

## Deliverables

| Deliverable | Description |
|---|---|
| Open-source attestation library | Rust crate for TPM 2.0 quote generation and verification |
| SPIFFE/SPIRE integration | SPIRE server + k3s workload attestation working demo |
| Security writeup series | 3 deep dives: TPM internals, FIDO FDO protocol, Confidential Computing |
| Conference talk / paper | Abstract submitted to USENIX Security, PETS, or IEEE S&P |
| Patent continuation | Follow-on technical contribution building on PCT/IB2023/063389 |

---

## Resources

- TCG TPM 2.0 Specification (Part 1–4) — primary reference
- IETF RATS Working Group RFCs — attestation standardization
- FIDO FDO Specification (FIDO Alliance)
- *Practical Cryptography for Developers* — free online
- Keylime project (open-source TPM attestation)
- Parsec project (hardware security abstraction layer)
- Sigstore documentation (supply chain signing)
