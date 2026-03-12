# Auto-Deploy Flask App with CI/CD

## About the Project

Pet project to demonstrate **DevOps Engineer** skills. Full CI/CD cycle implemented:
- Automatic Docker image build
- Publication to Docker Hub
- Deployment to VPS via SSH

## Architecture

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

## Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.11, Flask |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Web Server** | Nginx (reverse proxy) |
| **Infrastructure** | Ubuntu 22.04, VPS |
| **Image Registry** | Docker Hub |