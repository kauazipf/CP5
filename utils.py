import csv
from typing import List, Dict, Optional

CSV_PATH = "bd.csv"

def carregar_dados() -> List[Dict[str, str]]:
    with open(CSV_PATH, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def salvar_dados(dados: List[Dict[str, str]]):
    with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["ID", "Tabela", "Nome", "Descrição", "Quantidade", "Preço"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dados)

def buscar_por_id(id: str, tabela: str) -> Optional[Dict[str, str]]:
    for item in carregar_dados():
        if item["ID"] == id and item["Tabela"] == tabela:
            return item
    return None
