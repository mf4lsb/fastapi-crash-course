from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str
    description: Optional[str] = None

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

@app.post("/package/", response_model=Package, response_model_exclude={"description"}) # exclude mean doesn't show parameter in response, but the other one include is just show the paramter. response_model_exclude_unset is boolean value (True), will not show if Optional value isn't fill
async def make_package(package: PackageIn):
    return package