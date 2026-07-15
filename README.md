# To-Do API — com Autenticação, Projetos, Subtarefas e Dashboard

API de gerenciamento de tarefas construída com FastAPI + PostgreSQL.

## Status do desenvolvimento

- [x] Etapa 0 — Setup do ambiente
- [x] Etapa 1 — Modelagem de dados
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
docker compose up --build

# 2. Acesse a documentação interativa
http://localhost:8000/docs

# 3. Teste o health check
curl http://localhost:8000/health
```

Se tudo estiver certo, `/health` deve responder:
```json
{"status": "ok", "service": "To-Do API"}
```

## Rodando as migrations (Etapa 1)

Com os containers no ar (`docker compose up`), rode em outro terminal:

```bash
docker compose exec api alembic upgrade head
```

Isso cria as tabelas `users`, `projects` e `tasks` no Postgres.

Para gerar novas migrations no futuro (depois de alterar um model):

```bash
docker compose exec api alembic revision --autogenerate -m "descrição da mudança"
docker compose exec api alembic upgrade head
```

## Modelo de dados

```
User
 └── Project (owner_id)
      └── Task (project_id)
           └── Task (parent_task_id → subtarefa)
```

Campos de `Task` relevantes:
- `status`: pending | in_progress | done
- `priority`: low | medium | high
- `estimated_minutes`: tempo estimado em minutos
- `due_date`: prazo de entrega
- `created_at` / `completed_at`: usados na Etapa 6 (dashboard)

## Estrutura de pastas

```
todo-api/
├── app/
│   ├── core/          # configurações e conexão com banco
│   ├── models/         # modelos SQLAlchemy (Etapa 1)
│   ├── routers/         # endpoints (Etapa 2+)
│   └── main.py         # ponto de entrada
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env.example
```

## Stack

- FastAPI + Uvicorn
- PostgreSQL + SQLAlchemy 2.0 + Alembic (migrations)
- JWT (python-jose) + bcrypt (passlib) para autenticação
- Pytest + httpx para testes
