from fastapi import FastAPI
from rotas import router
app = FastAPI()

banco_de_dados = []

app.include_router(router, prefix="")

# @app.get("/")
# def read_root(user_agent: Optional[str] = Header(None)):
#     return{"user_agent" : user_agent}

# @app.get("/cookie")
# def cookie(response : Response):
#     response.set_cookie(key="meucookie", value="1234")
#     return{"cookie": True}

# @app.get("/get-cookie")
# def get_cookie(meucookie: Optional[str] = Cookie(None)):
#     return{"Cookie": meucookie}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, p:bool, q: Optional[str] = None):
#     return{"item_id": item_id, "q": q, "p": p}

# @app.post("/item")
# def add_item(novo_item: Item, outro_item: Item):
#     return [novo_item, outro_item]