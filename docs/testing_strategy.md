# Estrategia de Pruebas

- **Unitarias**: funciones de features, validación de payload, clientes HTTP (mocks).
- **Integración**: contrato `/predict` ↔ middleware (WireMock/MockWebServer).
- **E2E (TEST env)**: flujo BY → middleware → ml-service → BY.
- **No funcionales**: carga (k6), resiliencia (fallo del ml-service).
- **Evidencias**: capturas/trace + registros `sl_msg_log`.
