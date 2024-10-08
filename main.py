from typing import Union
from fastapi import FastAPI, Header, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins
)


@app.get("/", tags=["Root"])
def read_root(token: Annotated[str | None, Header()] = None):
    if token is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="actualmente no tiene permisos",
                headers={"auth": "Bienvenido a la api de darkhusky"}, # se contesta como consideres el error
            )
    return {"ms": "Bienvenido a la api de darkhusky", "accede": "http://198.211.106.31/items/1?q=nos_destruiran_a_todos"}


@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
