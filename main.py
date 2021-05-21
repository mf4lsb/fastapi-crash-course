from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

app = FastAPI()

@app.get('/')
async def hello_world():
    return {"hello": "world"}

# # Path parameter
# @app.get('/component/{component_id}')
# async def get_component(component_id: int):
#     return {"component_id": component_id}

# # Query Parameter
# @app.get('/component')
# async def read_component(number:int, text: Optional[str]):
#     return {"number": number, "text": text}

@app.post("/package/{priority}")
async def make_package(priority: int, package: Package, value: bool):
    return {"priority": priority, **package.dict(), "value": value}