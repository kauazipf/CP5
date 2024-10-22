from fastapi import APIRouter, HTTPException, status
from typing import List, Dict
from utils import carregar_dados, salvar_dados, buscar_por_id

router = APIRouter()

@router.get("/", response_model=List[Dict[str, str]])
def listar_fornecedores():
    fornecedores = [item for item in carregar_dados() if item["Tabela"] == "Fornecedor"]
    return fornecedores

@router.post("/", status_code=status.HTTP_201_CREATED)
def adicionar_fornecedor(fornecedor: Dict[str, str]):
    fornecedor["ID"] = str(len(carregar_dados()) + 1)
    fornecedor["Tabela"] = "Fornecedor"
    dados = carregar_dados() + [fornecedor]
    salvar_dados(dados)
    return fornecedor

@router.put("/{id}", response_model=Dict[str, str])
def atualizar_fornecedor(id: str, updates: Dict[str, str]):
    fornecedor = buscar_por_id(id, "Fornecedor")
    if not fornecedor:
        raise HTTPException(404, "Fornecedor não encontrado.")
    fornecedor.update(updates)
    salvar_dados(carregar_dados())
    return fornecedor

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_fornecedor(id: str):
    dados = [item for item in carregar_dados() if item["ID"] != id or item["Tabela"] != "Fornecedor"]
    salvar_dados(dados)
