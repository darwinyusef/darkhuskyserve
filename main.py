from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins
)


@app.get("/")
def read_root():
    return {"ms": "la respuesta se ha generado con exito", "color": "red"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
