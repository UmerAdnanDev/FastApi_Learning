from fastapi import FastAPI
app = FastAPI()
@app.get('/')
async def home():
  # return "Welcome to Homepage"for json use dict
  return {'msg':'Welcome to Home Page'} 
@app.get('/dic')
def dic():
  return {'dic':'This is a python dictionary'}
@app.get('/greeting/{name}')
async def greet(name:str) -> dict:
  return {"greeting": f"Hi , {name}"}
@app.get("/age/{age}")
async def age(age:int) -> dict:
  return {"your age is ": age}
