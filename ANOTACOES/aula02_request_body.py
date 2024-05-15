#Criar um objeto do tipo Base model

#importar a BaseModel
from pydantic import BaseModel


# criar a classe
class Item(BaseModel):
    id : int
    descricao : str
    valor : float


#Criar o endpoint
@app.post("/item")
def add_item(novo_item: Item):
    return novo_item


#É possivel inclui mais de um item no endpoint
@app.post("/item")
def add_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]