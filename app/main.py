from fastapi import FastAPI

from app.core.config import settings
from app.routers import auth

app = FastAPI(
    title=settings.project_name,
    version=settings.api_version,
    description="API de gerenciamento de tarefas com autenticação, projetos, "
                 "subtarefas e dashboard de produtividade.",
)

app.include_router(auth.router)


@app.get("/health", tags=["Sistema"])
def health_check():
    """Endpoint simples para confirmar que a API e a conexão estão de pé."""
    return {"status": "ok", "service": settings.project_name}

