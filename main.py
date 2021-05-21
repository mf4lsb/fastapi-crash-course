from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello_world():
    return {"hello": "world"}

# Path parameter
@app.get('/component/{component_id}')
async def get_component(component_id: int):
    return {"component_id": component_id}

# Query Parameter
@app.get('/component')
async def read_component(number:int, text: Optional[str]):
    return {"number": number, "text": text}