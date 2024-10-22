import csv

CSV_PATH = "bd.csv"

def adicionar_dado():
    tabela = input("Informe o tipo (Produto, Fornecedor, Pedido): ").strip().capitalize()
    nome = input("Nome: ").strip()
    descricao = input("Descrição: ").strip()
    quantidade = input("Quantidade: ").strip() or "0"
    preco = input("Preço: ").strip() or "0.00"

    # Geração automática de ID
    with open(CSV_PATH, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        dados = list(reader)
        novo_id = len(dados) + 1

    # Criação do novo registro
    novo_registro = {
        "ID": str(novo_id),
        "Tabela": tabela,
        "Nome": nome,
        "Descrição": descricao,
        "Quantidade": quantidade,
        "Preço": preco,
    }

    # Adiciona o registro ao CSV
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=novo_registro.keys())
        writer.writerow(novo_registro)

    print(f"{tabela} adicionado com sucesso!")

if __name__ == "__main__":
    while True:
        adicionar_dado()
        continuar = input("Deseja adicionar mais um? (s/n): ").strip().lower()
        if continuar != "s":
            break
