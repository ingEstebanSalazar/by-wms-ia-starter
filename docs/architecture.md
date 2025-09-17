# Arquitectura

**Opción recomendada (performante y modular):**
- **ml-service (Python)**: FastAPI + XGBoost → latencia baja en tabular, fácil de versionar.
- **middleware (Spring Boot)**: orquesta llamadas, enriquece features, aplica reglas, controla reintentos.
- **BY WMS**: políticas de habilitación por bodega, hooks (MOCA / do http request), evidencias en `sl_msg_log`.

## Flujo
1. Evento BY (ej: creación de tarea de picking) → Middleware.
2. Middleware consulta DB/vistas para features → llama a `ml-service:/predict`.
3. Middleware aplica regla de negocio y actualiza prioridad/seq/atributos en BY.
4. Log de auditoría (payload + score) en `sl_msg_log` / logs app.
