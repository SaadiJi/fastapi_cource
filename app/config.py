from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str = "1234567"
    database_name: str = "postgres"
    database_username: str = "postgres"
    secret_key: str = "67yu89koloi9878ko"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
        
    #model_config = SettingsConfigDict(env_file=".env")
    
    class Config:
        env_file = ".env"
    
settings = Settings()