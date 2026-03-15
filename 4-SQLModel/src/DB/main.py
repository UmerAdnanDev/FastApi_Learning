from sqlmodel import create_engine,text,SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
engine = AsyncEngine(
   create_engine(
   url=Config.DATABASE_URL,echo=True # type: ignore
))
async def init_db():
   async with engine.begin() as conn:
     from src.products.models import Product
     await conn.run_sync(SQLModel.metadata.create_all) 
async def get_session()-> AsyncSession: # type: ignore
   Session = sessionmaker(
      bind = engine,class_=AsyncSession, # type: ignore
      expire_on_commit=False # allows to use session object even after commiting db transactions
   ) # type: ignore
   async with Session() as session: # type: ignore
      yield session # type: ignore