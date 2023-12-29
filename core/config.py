from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class DataBaseSettings(BaseSettings):
    user: str = ...
    password: str = ...
    db: str = ...
    host: str = ...
    port: int = ...

    model_config = SettingsConfigDict(env_prefix='postgres_')


class Settings(BaseSettings):
    debug_mode: bool = False

    project_name: str = 'Url shortener'

    db: DataBaseSettings = DataBaseSettings()
    database_dsn: str = f'asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.db}'


settings = Settings()
