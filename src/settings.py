from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5434/ads_db"

    postgres_host: str | None = None
    postgres_port: int | None = None
    postgres_database_name: str | None = None
    postgres_username: str | None = None
    postgres_password: str | None = None

    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"

    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_brokers: str | None = None

    kafka_topic_ads: str = "ads"
    kafka_topic_marketplace_ads: str | None = None

    auth_service_url: str = "http://localhost:8000"

    def get_database_url(self) -> str:
        if self.postgres_host:
            return (
                f"postgresql+asyncpg://{self.postgres_username}:"
                f"{self.postgres_password}@{self.postgres_host}:"
                f"{self.postgres_port}/{self.postgres_database_name}"
            )
        return self.database_url

    def get_kafka_bootstrap_servers(self) -> str:
        return self.kafka_brokers or self.kafka_bootstrap_servers

    def get_kafka_topic_ads(self) -> str:
        return self.kafka_topic_marketplace_ads or self.kafka_topic_ads
