# MLOps

- **MLflow**: rastreo de runs (params, metrics), registry de modelos.
- **Versionado**: SemVer en modelos (v1.0.0), Git tags en código.
- **CI/CD**: build + test + docker build + push a registry.
- **Monitoreo**: métricas (p95 latencia), 4xx/5xx, tasa de timeout, drift (KS-test sencillo).
- **Rollback**: pin del modelo en `MODEL_VERSION` y redeploy.
