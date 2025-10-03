# homelab-compliance-automation

A self-hosted, Vanta-like compliance automation stack for the FatTwin homelab.  
Focus: continuous scans, evidence collection, policy-as-code, dashboards, and tamper-evident audit trails.

## Capabilities
- Continuous compliance scans (CIS, NIST, PCI, HIPAA, SOC 2 mapping)
- Evidence collection from Proxmox, OPNsense, Kubernetes, and apps
- Grafana scorecards + trends, Wazuh compliance views
- Policy-as-code (Kyverno, OPA/Conftest) and runtime (Falco)
- Immutable evidence (Git history; optional Rekor transparency log)
- Automation via GitHub Actions + n8n

## Quick Start
1. Deploy scanners (kube-bench, Trivy Operator) to your cluster.
2. Run `compliance-automation/evidence-collector/ansible-playbooks/*` to pull configs from Proxmox/OPNsense/Authentik.
3. Point Grafana at Loki/JSON exporters and import dashboards from `compliance-automation/dashboards/grafana/`.
4. Enable `.github/workflows/weekly-compliance.yml` and `evidence-commit.yml` (use a self-hosted runner or GitHub-hosted as desired).
5. (Optional) Integrate Cosign/Rekor for signed attestations.

> **Safety**: Only scan systems you own or are authorized to test.
