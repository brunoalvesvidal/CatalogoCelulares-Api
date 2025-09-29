from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/celulares", tags=["Celulares"])

celulares = [
    {"id": 1, "nome": "iPhone 14", "preco": 7000},
    {"id": 2, "nome": "Samsung Galaxy S23", "preco": 5000},
    {"id": 3, "nome": "Xiaomi 13 Pro", "preco": 4500},
]

class Item(BaseModel):
    nome: str
    preco: float

@router.get("/")
def listar_celulares():
    return {"Items": celulares}

@router.post("/")
def adicionar_celular(produto: Item):
    novo_id = len(celulares) + 1
    novo_celular = {"id": novo_id, "nome": produto.nome, "preco":produto.preco}
    celulares.append(novo_celular)
    return{"mensagem": "Celular adicionado com sucesso!", "produto" : novo_celular}