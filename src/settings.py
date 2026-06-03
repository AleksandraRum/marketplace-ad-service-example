from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    database_url: str | None = None

    postgres_host: str | None = None
    postgres_port: int | None = None
    postgres_database_name: str | None = None
    postgres_username: str | None = None
    postgres_password: str | None = None

    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"

    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic_ads: str = "ads"

    auth_service_url: str = "http://localhost:8000"

    def get_database_url(self) -> str:
        if self.database_url:
            return self.database_url

        return (
            f"postgresql+asyncpg://{self.postgres_username}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_database_name}"
        )
