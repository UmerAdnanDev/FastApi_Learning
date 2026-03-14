from pydantic import BaseModel 
import uuid
from datetime import datetime
class Product(BaseModel):
  uuid: uuid.UUID
  name: str
  price: float
  publish_date: str
  created_at: datetime
  updated_at: datetime
class ProductCreateModel(BaseModel):
  name: str
  price: float
  publish_date: str
class ProductUpdateModel(BaseModel):
  name: str
  price: float