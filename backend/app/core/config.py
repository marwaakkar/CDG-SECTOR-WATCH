from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CDG Sector Watch"
    api_v1_prefix: str = "/api/v1"
    environment: str = "development"
    backend_cors_origins: str = "http://localhost:3000"
    llm_provider: str = "mock"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.backend_cors_origins.split(",") if origin.strip()]


settings = Settings()
