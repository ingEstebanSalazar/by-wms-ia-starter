# Roadmap · 12 Semanas (IA + BY WMS)

## Semana 1–2 · Fundamentos y entorno
- Python 3.11, virtualenv/poetry, notebooks.
- NumPy, Pandas, matplotlib.
- ML básico: train/test, métricas, overfitting.
- Docker, Git, ramas (main/dev/feature/*).
**Entregables:** Notebook de exploración + guía de entorno.

## Semana 3–4 · Modelos tabulares (WMS-like)
- XGBoost/LightGBM/CatBoost.
- Pipelines: imputación, encoding, escalado.
- k-fold, RandomSearch/GridSearch.
**Proyecto 1:** ETA Picking (regresión).

## Semana 5–6 · Serving de modelos
- FastAPI + Pydantic + joblib.
- Serialización de artefactos.
- Dockerfile slim, healthcheck.
**Proyecto 2:** Microservicio `/predict`.

## Semana 7–8 · Integración con Spring Boot
- WebFlux/WebClient, timeouts, retries.
- Resilience4j (circuit breaker).
- Mapeo a campos BY (MOCA/endpoints).
**Proyecto 3:** Middleware que orquesta.

## Semana 9–10 · MLOps
- MLflow (experimentos y artefactos).
- DVC (opcional) para datos.
- GitHub Actions (build, test, docker push).
**Proyecto 4:** Pipeline CI/CD.

## Semana 11–12 · Casos BY y despliegue
- Slotting, anomalías inventario, forecast.
- Observabilidad (latencia, errores, drift).
- Pruebas en ambiente TEST y hard bounce.
**Proyecto 5:** PoC operacional.
