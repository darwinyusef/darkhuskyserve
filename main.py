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


@app.get("/")
def read_root(token: Annotated[str | None, Header()] = None):
    if token is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="actualmente no tiene permisos",
                headers={"auth": "Bienvenido a la api de darkhusky"}, # se contesta como consideres el error
            )
    return {"ms": "Bienvenido a la api de darkhusky", "warnings": "actualmente no tiene permisos"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
