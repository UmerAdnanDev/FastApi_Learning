from fastapi import FastAPI
from src.products.routes import product_router
version = "v1"
app = FastAPI(version=version,
              title="Modular Product Crud",
              description="A RestAPI for product web service")

app.include_router(product_router)
#to run
# cd 3-Routers
#uvicorn src.main:app --reload --port 8002

