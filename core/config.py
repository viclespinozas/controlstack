from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    # TEMP MONGO SETTINGS TO BE REPLACED IN TRANSACTIONS CARD
    mongo_uri: str = Field(alias='MONGO_URI', default='mongodb://db:27017')
    database_name: str = Field(alias='MONGO_DB', default='controlstack')

    database_url: str = Field(alias='DATABASE_URL')
    sql_logging: bool = Field(alias='SQL_LOGGING', default=False)

settings = Settings()