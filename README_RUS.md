# Auto-Deploy Flask App with CI/CD

## О проекте

Пет-проект для демонстрации навыков **DevOps Engineer**. Реализован полный цикл CI/CD:
- Автоматическая сборка Docker-образа
- Публикация в Docker Hub
- Деплой на VPS по SSH

---

## Архитектура

```mermaid
graph TB
    A[Developer] -->|git push| B(GitHub Repository)
    B --> C{GitHub Actions}
    C -->|Build| D[Docker Image]
    D -->|Push| E[(Docker Hub)]
    E -->|Pull| F[VPS Server]
    F -->|Deploy| G[Docker Compose]
    G --> H[Nginx :80]
    G --> I[Flask App :5000]
    H -->|Proxy| I
```

---

## Стек технологий

| Категория | Инструменты |
|-----------|-------------|
| **Язык** | Python 3.11, Flask |
| **Контейнеризация** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Веб-сервер** | Nginx (reverse proxy) |
| **Инфраструктура** | Ubuntu 22.04, VPS |
| **Реестр образов** | Docker Hub |