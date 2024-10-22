import sqlite3

# Conecta ao banco de dados (ou cria, se não existir)
conexao = sqlite3.connect('sistema_geral.db')
cursor = conexao.cursor()

# Criação das tabelas de Produtos, Fornecedores e Pedidos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    data_fabricacao TEXT NOT NULL,
    data_validade TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cnpj TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT,
    endereco TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data_pedido TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

conexao.commit()

# Funções de Produtos
def cadastrar_produto():
    nome = input("Nome do Produto: ")
    preco = float(input("Preço: "))
    data_fabricacao = input("Data de Fabricação (DD-MM-YYYY): ")
    data_validade = input("Data de Validade (DD-MM-YYYY): ")

    cursor.execute('''
        INSERT INTO produtos (nome, preco, data_fabricacao, data_validade)
        VALUES (?, ?, ?, ?)
    ''', (nome, preco, data_fabricacao, data_validade))
    conexao.commit()
    print("Produto cadastrado com sucesso!\n")

def exibir_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto cadastrado.\n")
    else:
        for produto in produtos:
            print(" \n ============== // ============= \n")
            print(f"\nID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:.2f}")
            print(f"Fabricação: {produto[3]} | Validade: {produto[4]}")
            print("\n ============== // ============= \n")
            
def atualizar_produto():
    exibir_produtos()
    produto_id = input("Digite o ID do produto a ser atualizado: ")

    nome = input("Novo nome: ")
    preco = float(input("Novo preço: "))
    data_fabricacao = input("Nova data de fabricação (YYYY-MM-DD): ")
    data_validade = input("Nova data de validade (YYYY-MM-DD): ")

    cursor.execute('''
        UPDATE produtos
        SET nome = ?, preco = ?, data_fabricacao = ?, data_validade = ?
        WHERE id = ?
    ''', (nome, preco, data_fabricacao, data_validade, produto_id))
    conexao.commit()
    print("Produto atualizado com sucesso!\n")

def deletar_produto():
    exibir_produtos()
    produto_id = input("Digite o ID do produto a ser deletado: ")

    cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    conexao.commit()
    print("Produto deletado com sucesso!\n")

# Funções de Fornecedores
def cadastrar_fornecedor():
    nome = input("Nome do Fornecedor: ")
    cnpj = input("CNPJ: ")
    telefone = input("Telefone: ")
    email = input("Email (opcional): ")
    endereco = input("Endereço (opcional): ")

    cursor.execute('''
        INSERT INTO fornecedores (nome, cnpj, telefone, email, endereco)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, cnpj, telefone, email, endereco))
    conexao.commit()
    print("Fornecedor cadastrado com sucesso!\n")

def exibir_fornecedores():
    cursor.execute("SELECT * FROM fornecedores")
    fornecedores = cursor.fetchall()

    if not fornecedores:
        print("Nenhum fornecedor cadastrado.\n")
    else:
        for fornecedor in fornecedores:
            print("\n ============== // ============= \n")
            print(f"\nID: {fornecedor[0]} | Nome: {fornecedor[1]}")
            print(f"CNPJ: {fornecedor[2]} | Telefone: {fornecedor[3]}")
            print(f"Email: {fornecedor[4]} | Endereço: {fornecedor[5]}")
            print("\n ============== // ============= \n")
            
def atualizar_fornecedor():
    exibir_fornecedores()
    fornecedor_id = input("Digite o ID do fornecedor a ser atualizado: ")

    nome = input("Novo nome: ")
    cnpj = input("Novo CNPJ: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email (opcional): ")
    endereco = input("Novo endereço (opcional): ")

    cursor.execute('''
        UPDATE fornecedores
        SET nome = ?, cnpj = ?, telefone = ?, email = ?, endereco = ?
        WHERE id = ?
    ''', (nome, cnpj, telefone, email, endereco, fornecedor_id))
    conexao.commit()
    print("Fornecedor atualizado com sucesso!\n")

def deletar_fornecedor():
    exibir_fornecedores()
    fornecedor_id = input("Digite o ID do fornecedor a ser deletado: ")

    cursor.execute("DELETE FROM fornecedores WHERE id = ?", (fornecedor_id,))
    conexao.commit()
    print("Fornecedor deletado com sucesso!\n")

# Funções de Pedidos
def cadastrar_pedido():
    nome_cliente = input("Nome do Cliente: ")
    produto = input("Nome do Produto: ")
    quantidade = int(input("Quantidade: "))
    data_pedido = input("Data do Pedido (DD-MM-YYYY): ")
    status = input("Status (Pendente/Entregue/Cancelado): ")

    cursor.execute('''
        INSERT INTO pedidos (nome_cliente, produto, quantidade, data_pedido, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome_cliente, produto, quantidade, data_pedido, status))
    conexao.commit()
    print("Pedido cadastrado com sucesso!\n")

def exibir_pedidos():
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()

    if not pedidos:
        print("Nenhum pedido cadastrado.\n")
    else:
        for pedido in pedidos:
            print("\n ============== // ============= \n")
            print(f"\nID: {pedido[0]} | Cliente: {pedido[1]}")
            print(f"Produto: {pedido[2]} | Quantidade: {pedido[3]}")
            print(f"Data: {pedido[4]} | Status: {pedido[5]}")
            print("\n ============== // ============= \n")
            
def atualizar_pedido():
    exibir_pedidos()
    pedido_id = input("Digite o ID do pedido a ser atualizado: ")

    nome_cliente = input("Novo nome do cliente: ")
    produto = input("Novo produto: ")
    quantidade = int(input("Nova quantidade: "))
    data_pedido = input("Nova data do pedido (YYYY-MM-DD): ")
    status = input("Novo status (Pendente/Entregue/Cancelado): ")

    cursor.execute('''
        UPDATE pedidos
        SET nome_cliente = ?, produto = ?, quantidade = ?, data_pedido = ?, status = ?
        WHERE id = ?
    ''', (nome_cliente, produto, quantidade, data_pedido, status, pedido_id))
    conexao.commit()
    print("Pedido atualizado com sucesso!\n")

def deletar_pedido():
    exibir_pedidos()
    pedido_id = input("Digite o ID do pedido a ser deletado: ")

    cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
    conexao.commit()
    print("Pedido deletado com sucesso!\n")