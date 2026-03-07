from sqlmodel import SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid 
class Product(SQLModel,table = True):
  __tablename__="products" # type: ignore
  uid: uuid.UUID = Field(
    sa_column=Column(
      pg.UUID,nullable=False,
      primary_key=True,default=uuid.uuid4()
    )

  )
  name: str
  price: float
  created_at:datetime = Field(Column(pg.TIMESTAMP,default=datetime.now))
  updated_at:datetime =  Field(Column(pg.TIMESTAMP,default=datetime.now))
  def __repr__(self):
    return f"<product {self.name}>"
