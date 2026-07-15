from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.project_name,
    version=settings.api_version,
    description="API de gerenciamento de tarefas com autenticação, projetos, "
                 "subtarefas e dashboard de produtividade.",
)


@app.get("/health", tags=["Sistema"])
def health_check():
    """Endpoint simples para confirmar que a API e a conexão estão de pé."""
    return {"status": "ok", "service": settings.project_name}


# A partir da Etapa 1 (Modelagem), os routers de auth, projects, tasks e stats
# serão incluídos aqui com app.include_router(...)
