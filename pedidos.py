from fastapi import APIRouter, HTTPException, status
from typing import List, Dict
from utils import carregar_dados, salvar_dados, buscar_por_id

router = APIRouter()

@router.get("/", response_model=List[Dict[str, str]])
def listar_pedidos():
    pedidos = [item for item in carregar_dados() if item["Tabela"] == "Pedido"]
    return pedidos

@router.post("/", status_code=status.HTTP_201_CREATED)
def adicionar_pedido(pedido: Dict[str, str]):
    pedido["ID"] = str(len(carregar_dados()) + 1)
    pedido["Tabela"] = "Pedido"
    dados = carregar_dados() + [pedido]
    salvar_dados(dados)
    return pedido

@router.put("/{id}", response_model=Dict[str, str])
def atualizar_pedido(id: str, updates: Dict[str, str]):
    pedido = buscar_por_id(id, "Pedido")
    if not pedido:
        raise HTTPException(404, "Pedido não encontrado.")
    pedido.update(updates)
    salvar_dados(carregar_dados())
    return pedido

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_pedido(id: str):
    dados = [item for item in carregar_dados() if item["ID"] != id or item["Tabela"] != "Pedido"]
    salvar_dados(dados)
