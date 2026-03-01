from fastapi import FastAPI
from typing import Optional
app = FastAPI()
# basic get request returning a text
# http://127.0.0.1:8000/
@app.get('/')
async def home():
  return {'Welcome to Home Page'}
# basic get request returning a dict / json data 
#http://127.0.0.1:8000/dict
@app.get('/dict')
def dic():
  return {'dict':'This is a python dictionary'}

# using name string type of path variable
# http://127.0.0.1:8000/greeting/Adnan 
@app.get('/greeting/{name}')
async def greet(name:str) -> dict:
  return {"greeting": f"Hi , {name}"}

# using age int type of path variable 
# http://127.0.0.1:8000/age/19 
@app.get("/age/{age}")
async def age(age:int) -> dict:
  return {"your age is ": age}

#using query parameter to send data/ value
#http://127.0.0.1:8000/usequery?name=umer&age=19
@app.get("/usequery")
async def querycheck(name:str,age:int)-> dict:
  return {"message":f"Your name is {name} and age is {age}"}

'''using Optional for default values of variables to avoid null error if no query entered'''
#http://127.0.0.1:8000/opquery
# or http://127.0.0.1:8000/opquery?name=umer&age=19 or either 
@app.get("/opquery")
async def optionalquery(name:Optional[str]="Default-Name",age:Optional[int]=0)-> dict:
  return {"message":f"Your name is {name} and age is {age}"}
#same thing even without optional but here is a difference 
'''in Optional use name variable can be either str or None (Empty)
 but without it it needs to be string (str)
(either in default value or web query ?age = None is possible in Optinal method)'''
@app.get("/noquery")
async def noquery(name:str ="Default-Name",age:int=0)-> dict:
  return {"message":f"Your name is {name} and age is {age}"}