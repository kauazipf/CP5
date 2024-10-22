from fastapi import APIRouter, HTTPException, status
from typing import List, Dict
from utils import carregar_dados, salvar_dados, buscar_por_id

router = APIRouter()

@router.get("/", response_model=List[Dict[str, str]])
def listar_produtos():
    produtos = [item for item in carregar_dados() if item["Tabela"] == "Produto"]
    return produtos

@router.post("/", status_code=status.HTTP_201_CREATED)
def adicionar_produto(produto: Dict[str, str]):
    produto["ID"] = str(len(carregar_dados()) + 1)
    produto["Tabela"] = "Produto"
    dados = carregar_dados() + [produto]
    salvar_dados(dados)
    return produto

@router.put("/{id}", response_model=Dict[str, str])
def atualizar_produto(id: str, updates: Dict[str, str]):
    produto = buscar_por_id(id, "Produto")
    if not produto:
        raise HTTPException(404, "Produto não encontrado.")
    produto.update(updates)
    salvar_dados(carregar_dados())
    return produto

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(id: str):
    dados = [item for item in carregar_dados() if item["ID"] != id or item["Tabela"] != "Produto"]
    salvar_dados(dados)
