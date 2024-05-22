# Criar a pasta models na raiz do projeto  e dentro dela criar o arquivo papel.py e __ini__.py
# criar um arquivo __init__.py na raiz do projeto.
# papel.py

from pydantic import BaseModel

class Papel(BaseModel):
    id: int
    nome: str
    sigla: str
    cnpj: str

# Criar um arquivo __init__.py na raiz do projeto


# Criar a pasta controllers na raiz do projeto  e dentro dela criar o arquivo papeis_controller.py:
from fastapi import APIRouter
from models.papel import Papel

router = APIRouter()

banco_de_dados = []

@router.post("/")
def add_item(item: Papel):
    banco_de_dados.append(item)
    return item

@router.get("/")
def list_item():
    return banco_de_dados



# Criar o arquivo rotas.py na raiz do projeto:
from fastapi import APIRouter
from controllers import papeis_controller as papeis

router = APIRouter()

router.include_router(papeis.router, prefix='/papeis')



# No arquivo main.py remover as importacoes desnecessarias:
from fastapi import FastAPI
from rotas import router
app = FastAPI()

banco_de_dados = []

app.include_router(router, prefix="")