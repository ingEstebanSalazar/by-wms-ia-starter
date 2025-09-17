# Sprint 02 · Middleware + integración básica
**Objetivo:** Spring Boot WebFlux que consuma `/predict` y exponga un endpoint demo.

## Historias
- US-005: Crear proyecto Spring Boot (WebFlux).
- US-006: Implementar `PredictionClient` con timeouts y retries.
- US-007: `GET /demo/eta` que use `/predict` y devuelva recomendación.
- US-008: Pruebas de contrato + WireMock.

## Criterios de aceptación
- [ ] `GET /demo/eta` funcional con ml-service levantado.
- [ ] Timeouts configurados, fallback básico.
