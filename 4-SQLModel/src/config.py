from pydantic_settings import BaseSettings,SettingsConfigDict 
class Settings(BaseSettings):
  DATABASE_URL : str
  model_config = SettingsConfigDict(
    env_file='.env',
    extra="ignore"
  )
# python -c "import sys; sys.path.append('4-SQLModel'); from src.config import Settings; print(Settings().DATABASE_URL)"
#run on powershell to check
Config = Settings()  # type: ignore