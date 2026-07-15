from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configurações da aplicação, carregadas do arquivo .env.
    Centralizar aqui evita 'os.environ' espalhado pelo código.
    """
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Banco de dados
    database_url: str = "postgresql://todo_user:todo_pass@db:5432/todo_db"

    # Autenticação (usado a partir da Etapa 2)
    secret_key: str = "changeme-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # Metadados da API
    project_name: str = "To-Do API"
    api_version: str = "0.1.0"


settings = Settings()
