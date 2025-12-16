# Platform Explainability Architecture

## Signal Sources
- CI/CD pipelines
- Policy engines (Kyverno / OPA)
- Kubernetes events
- Metrics (Prometheus / VictoriaMetrics)
- Alerts
- Change metadata

## Explainability Flow
1. Event occurs
2. Context captured
3. Decision schema applied
4. Explanation generated
5. Stored as artefact

## Outputs
- JSON (machine)
- Markdown (human)
- Evidence bundle (audit)
