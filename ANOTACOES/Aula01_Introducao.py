# Instalar as bibliotecas
pip install fastapi
pip install uvicorn  #biblioteca para rodar local a API




# rodar o projeto
uvicorn main:app --reload    
# main = arquivo.py que inicia o projeto 
# app = app criada app = FastAPI()  
# reload para atulizar o que fopi alterado no projeto em tempo real



# arquivo main.py
from typing import Optional
from fastapi import FastAPI 


app = FastAPI()  

@app.get("/")  
def read_root():  
    return {'message': 'Olá Mundo!'}

@app.get("/items/{item_id}")
def read_item(item_id: int, p:bool, q: Optional[str] = None):
    return{"item_id": item_id, "q": q, "p": p}
