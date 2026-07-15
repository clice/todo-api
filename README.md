# To-Do API — com Autenticação, Projetos, Subtarefas e Dashboard

API de gerenciamento de tarefas construída com FastAPI + PostgreSQL.

## Status do desenvolvimento

- [x] Etapa 0 — Setup do ambiente
- [ ] Etapa 1 — Modelagem de dados
- [ ] Etapa 2 — Autenticação (JWT)
- [ ] Etapa 3 — CRUD de Projetos
- [ ] Etapa 4 — CRUD de Tarefas
- [ ] Etapa 5 — Subtarefas
- [ ] Etapa 6 — Dashboard de produtividade
- [ ] Etapa 7 — Testes automatizados
- [ ] Etapa 8 — Documentação final e deploy

## Como rodar (Etapa 0)

Pré-requisito: Docker e Docker Compose instalados.

```bash
# 1. Suba os containers (API + Postgres)
docker compose up --build -d

# 2. Acesse a documentação interativa
http://localhost:8000/docs

# 3. Teste o health check
curl http://localhost:8000/health
```

Se tudo estiver certo, `/health` deve responder:
```json
{"status": "ok", "service": "To-Do API"}
```

## Estrutura de pastas

    todo-api/
    ├── app/
    │   ├── core/           # configurações e conexão com banco
    │   ├── models/         # modelos SQLAlchemy (Etapa 1)
    │   ├── routers/        # endpoints (Etapa 2+)
    │   └── main.py         # ponto de entrada
    ├── docker-compose.yml
    ├── Dockerfile
    ├── requirements.txt
    └── .env.example

## Stack

- FastAPI + Uvicorn
- PostgreSQL + SQLAlchemy 2.0 + Alembic (migrations)
- JWT (python-jose) + bcrypt (passlib) para autenticação
- Pytest + httpx para testes
