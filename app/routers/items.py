from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/celulares", tags=["Celulares"])

celulares = [
    {"id": 1, "nome": "IphoneXR", "preco": 5000},
    {"id": 2, "nome": "Iphone15", "preco": 7000}
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

@router.get("/{produto_id}")
def buscar_produto (produto_id: int):
    for produto in celulares:
        if produto["id"] == produto_id:
            return produto
        
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.put("/{produto_id}", response_model=Item)
def atualizar_celular(produto_id: int, celular_atualizado: Item):
    for index, celular in enumerate(celulares):
        if celular["id"] == produto_id:
            celulares[index] = celular_atualizado
            return celular_atualizado
        raise HTTPException(status_code=404, detail="Celular não encontrado")