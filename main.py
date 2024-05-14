from typing import Optional
from fastapi import FastAPI 


app = FastAPI()  

@app.get("/")  
def read_root():  
    return {'message': 'Olá Mundo!'}

@app.get("/items/{item_id}")
def read_item(item_id: int, p:bool, q: Optional[str] = None):
    return{"item_id": item_id, "q": q, "p": p}