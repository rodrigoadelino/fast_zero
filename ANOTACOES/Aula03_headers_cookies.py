## Header
# Importar a classe Header
from fastapi import FastAPI, Header

#Criar o endpoint para pegar o user agente
@app.get("/")
def read_root(user_agent: Optional[str] = Header(None)):
    return{"user_agent" : user_agent}



## Cookies
# Importar a classe Response
from fastapi import FastAPI, Response

#Criar o endpoint para setar o cookie
@app.get("/cookie")
def cookie(response: Response):
    response.set_cookie(key="meucookie", value="1234")
    return{"cookie": True}


# Importar a classe Cookie
from fastapi import FastAPI, Cookie

#Criar enpoint para ler o Cookie
@app.get("/get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return{"Cookie": meucookie}