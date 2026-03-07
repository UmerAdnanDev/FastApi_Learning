from pydantic_settings import BaseSettings,SettingsConfigDict 
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent 
'''we are using this to use .env which is in root of main FASTAPI_LEARNING folder but we could have just created a new db if we had it in this projects root instead of sharing one DB accross all folders '''

class Settings(BaseSettings):
  DATABASE_URL : str
  model_config = SettingsConfigDict(
    env_file=BASE_DIR /'.env',
    extra="ignore"
  )
# python -c "import sys; sys.path.append('4-SQLModel'); from src.config import Settings; print(Settings().DATABASE_URL)"
#run on powershell to check
Config = Settings()  # type: ignore

# From FASTAPI_LEARNING root
#cd 4-SQLModel
#python -c "from src.config import Config; print(Config.DATABASE_URL)" to check if it can access .env