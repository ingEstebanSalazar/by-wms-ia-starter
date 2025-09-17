# BY WMS · IA Starter (Python + FastAPI + XGBoost | Spring Boot Middleware)

**Objetivo:** Acelerar la adopción de IA en procesos de BY WMS mediante un microservicio de predicción
(Python) y un middleware de integración (Spring Boot), con una **ruta de 12 semanas**, backlog de producto,
plantillas de sprints, pruebas y CI/CD.

> Fecha: 2025-09-17 · Autor: Juan Esteban (y equipo)

## Estructura
```
by-wms-ia-starter/
├─ docs/
│  ├─ roadmap.md
│  ├─ architecture.md
│  ├─ data_schema.md
│  ├─ mlops.md
│  ├─ testing_strategy.md
│  └─ sprints/
│     ├─ sprint-01.md
│     ├─ sprint-02.md
│     └─ templates/
│        ├─ sprint-template.md
│        └─ story-template.md
├─ ml-service/           # Microservicio Python (FastAPI) para predicción
│  ├─ app.py
│  ├─ train.py
│  ├─ requirements.txt
│  ├─ Dockerfile
│  └─ README.md
├─ middleware/           # Spring Boot (WebFlux) para orquestación
│  ├─ pom.xml
│  └─ src/main/java/com/example/bywms/
│     ├─ Application.java
│     ├─ client/PredictionClient.java
│     ├─ controller/DemoController.java
│     └─ model/Dto.java
├─ docker-compose.yml
├─ .github/
│  └─ workflows/ci.yml
└─ .github/ISSUE_TEMPLATE/
   ├─ bug_report.md
   └─ user_story.md
```

## Cómo arrancar rápido
```bash
# 1) Entrenar y levantar el microservicio de IA
cd ml-service
python -m pip install -r requirements.txt
python train.py
uvicorn app:app --reload --port 8000

# 2) Levantar middleware Spring Boot (requiere JDK 17+ y Maven 3.9+)
cd ../middleware
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Dspring.profiles.active=dev"
```
