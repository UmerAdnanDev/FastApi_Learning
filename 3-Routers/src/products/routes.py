from fastapi import APIRouter,status
from typing import List
from fastapi.exceptions import HTTPException
from .product_data import products
from .schemas import Product,ProductUpdateModel
product_router = APIRouter()

@product_router.get('/intro')
async def intro():
  return {"message":"A FastApi CRUD for products\nwith modular project structure\nusing routers"}
@product_router.get('/',response_model=List[Product]) # pydantic expects dict but we were fetching a list of dict so we imported List module
async def get_all_products():
  return products
@product_router.post('/',status_code=status.HTTP_201_CREATED)
async def create_products(product_data:Product)-> dict:
   new_product = product_data.model_dump() #coverts product_data into dict
   products.append(new_product)
   return new_product
@product_router.get('/{product_id}')
async def get_product(product_id:int) -> dict:
  for product in products:
    if product['id'] == product_id:
       return product
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product Not Found OF ID:{product_id}")
@product_router.patch('/{product_id}')
async def update_product(product_id:int,product_update_data:ProductUpdateModel)-> dict:
  for product in products:
    if product['id'] == product_id:
      product['name'] = product_update_data.name
      product['price'] = product_update_data.price
      return product
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product Not Found OF ID:{product_id}")
@product_router.delete('/{product_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id:int):
  for product in products:
    if product['id']==product_id:
      products.remove(product)
      return None # or {}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product Not Found OF ID:{product_id}")
