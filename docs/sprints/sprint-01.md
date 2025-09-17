# Sprint 01 · Fundamentos + PoC mínima
**Objetivo:** Entrenar un baseline y exponer `/predict` con datos sintéticos.

## Historias
- US-001: Preparar entorno Python + FastAPI + XGBoost.
- US-002: Generar dataset sintético WMS y entrenar baseline.
- US-003: Exponer endpoint `/predict` con validación.
- US-004: Dockerizar ml-service y healthcheck.

## Criterios de aceptación
- [ ] `train.py` genera `model.pkl` y métricas (MAE/RMSE).
- [ ] `POST /predict` responde `<50ms` en promedio local.
- [ ] Imagen Docker lista.
