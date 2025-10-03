# ROADMAP

## Phase 1 — Scanners
- [ ] kube-bench (K8s CIS)
- [ ] Trivy Operator (images, config posture)
- [ ] kube-hunter (on-demand)
- [ ] Lynis & OpenSCAP (VMs)

## Phase 2 — Evidence
- [ ] Ansible pullers (Proxmox, OPNsense, Authentik)
- [ ] Exporters to JSON/Markdown; commit to `compliance-automation/reports/json`

## Phase 3 — Dashboards
- [ ] Grafana scorecard + trends
- [ ] Wazuh compliance views

## Phase 4 — Policy-as-Code
- [ ] Kyverno baseline/restricted
- [ ] Conftest gates in CI
- [ ] Falco runtime rules

## Phase 5 — Audit & Attestation
- [ ] Rekor/Cosign attestations
- [ ] Quarterly signed PDF reports

## Phase 6 — DR & SLOs
- [ ] Automated restore drill with evidence
- [ ] Alert SLOs (time-to-triage, time-to-remediate)
