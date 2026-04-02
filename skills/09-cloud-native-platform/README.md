# Track 09 · Cloud-Native & Platform Engineering

> **Goal:** Master Kubernetes internals and platform engineering at scale. Build the infrastructure that makes other engineers more productive and systems more reliable.

---

## Why It Matters

You already operate k3s in production. This track systematizes that operational knowledge into the depth needed for senior platform engineering roles and system design interviews that involve cloud-native infrastructure.

---

## Core Knowledge

**Kubernetes Internals**
- Control plane: API server, etcd, scheduler, controller manager — how they interact
- Scheduler: predicates (filtering), priorities (scoring), custom schedulers
- Controllers: reconciliation loop, informers, work queue pattern
- CRD (Custom Resource Definition) + controller = Kubernetes Operator pattern
- API machinery: admission webhooks (mutating, validating), API aggregation

**Workload Management**
- Pod lifecycle, QoS classes (Guaranteed, Burstable, BestEffort)
- Resource requests vs. limits — CPU throttling vs. OOM kill behavior
- Horizontal Pod Autoscaler (HPA), Vertical Pod Autoscaler (VPA), KEDA
- StatefulSets vs. Deployments — storage identity and ordered rollout
- PodDisruptionBudget — safe rolling upgrades under load

**Networking (CNI layer)**
- Pod networking model: every Pod gets a routable IP
- CNI plugins: Flannel, Calico, Cilium (eBPF-based) — trade-offs
- Kubernetes Services: ClusterIP, NodePort, LoadBalancer, Headless
- Ingress vs. Gateway API — the evolution of L7 routing in k8s
- Network Policies — Pod-level firewall rules

**Storage (CSI layer)**
- PersistentVolume, PersistentVolumeClaim, StorageClass lifecycle
- CSI driver model — how storage plugins work
- Local volumes vs. network storage — latency and reliability trade-offs
- Volume snapshots and backup patterns

**Security (RBAC + Policy)**
- RBAC: Role, ClusterRole, RoleBinding — least-privilege design
- ServiceAccount token projection (OIDC-compatible)
- Pod Security Standards (Restricted, Baseline, Privileged)
- OPA/Gatekeeper vs. Kyverno — policy enforcement
- Secret management: sealed-secrets, external-secrets-operator, Vault integration

**Observability**
- Prometheus: metric types (counter, gauge, histogram, summary), PromQL
- Grafana dashboards: USE method (Utilization, Saturation, Errors), RED method (Rate, Errors, Duration)
- OpenTelemetry: traces, metrics, logs — unified instrumentation
- Loki for log aggregation, Tempo for distributed traces
- SLI/SLO/Error budget — SRE methodology applied to k8s workloads

**GitOps & CI/CD**
- Flux vs. ArgoCD — push vs. pull model
- Helm chart authoring — templates, values, dependencies
- Progressive delivery: canary, blue/green, feature flags
- SBOM generation and policy gating in CI pipelines

---

## How to Practice

1. **Build a Kubernetes operator** — custom controller that manages a stateful application (e.g., a database cluster or an attestation service)
2. **Implement a CNI plugin from scratch** (simplified) — understand how Pod networking actually works
3. **Build a full observability stack** — Prometheus + Grafana + Loki + Tempo on your k3s cluster, with SLO dashboards
4. **Design a multi-tenant GPU scheduling policy** — extend your existing AI platform with fair-share scheduling
5. **Integrate external-secrets-operator with Vault** — connect your k8s workloads to a hardware-backed secret store

---

## Deliverables

| Deliverable | Description |
|---|---|
| Kubernetes operator | CRD + controller managing a real stateful resource |
| Observability stack | Full Prometheus/Grafana/Loki/Tempo deployment with SLO dashboards |
| GPU scheduling design doc | Architecture for multi-tenant GPU fair-share in k3s |
| GitOps migration | Move at least one production workload to ArgoCD/Flux |

---

## Resources

- *Kubernetes in Action* — Marko Luksa — deepest k8s reference book
- Kubernetes source code: `pkg/scheduler/`, `pkg/controller/`
- Cilium eBPF documentation — best CNI deep-dive
- Prometheus documentation + PromQL tutorial
- Google SRE Book ch. 4–6 (SLI/SLO/Error Budget) — free online
- Operator SDK / Kubebuilder documentation
