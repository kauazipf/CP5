# Código principal

from menu import menu, menu_produtos, menu_pedidos, menu_fornecedor
from servicos import cadastrar_produto, cadastrar_fornecedor, cadastrar_pedido, exibir_fornecedores, exibir_pedidos, exibir_produtos, atualizar_fornecedor, atualizar_pedido, atualizar_produto, deletar_fornecedor, deletar_pedido, deletar_produto

# Código de execução do projeto
def main():
    while True:
        opcao = menu()
        if opcao == '1':
            print("Opção produtos selecionada. \n")
            opcao_produto = menu_produtos()
            if opcao_produto == "1":
                cadastrar_produto()
            elif opcao_produto == "2":
                exibir_produtos()
            elif opcao_produto == "3":
                atualizar_produto()
            elif opcao_produto == "4":
                deletar_produto()
            else:
                print("\n==================== // =====================\n")
                print("Opção inválida.")
                print("\n==================== // =====================\n")
        elif opcao == '2':
            print("Opção fornecedores selecionada. \n")
            opcao_fornecedores = menu_fornecedor()
            if opcao_fornecedores == "1":
                cadastrar_fornecedor()
            elif opcao_fornecedores == "2":
                exibir_fornecedores()
            elif opcao_fornecedores == "3":
                atualizar_fornecedor()
            elif opcao_fornecedores == "4":
                deletar_fornecedor()
            else:
                print("\n==================== // =====================\n")
                print("Opção inválida.")
                print("\n==================== // =====================\n")
        elif opcao == '3':
            print("Opção pedidos selecionada. \n")
            opcao_pedidos = menu_pedidos()
            if opcao_pedidos == "1":
                cadastrar_pedido()
            elif opcao_pedidos == "2":
                exibir_pedidos()
            elif opcao_pedidos == "3":
                atualizar_pedido()
            elif opcao_pedidos == "4":
                deletar_pedido()
            else:
                print("\n==================== // =====================\n")
                print("Opção inválida.")
                print("\n==================== // =====================\n")
        elif opcao == '4':
            print("Opção Participantes selecionada. \n")
            print("\n\tKauã Fermino Zipf \t RM-558957")
            print("\n\tCaetano Penafiel \t RM-557984")
            print("\n\tVictor Egidio Lira \t RM-556653")
            print("\n\tDiego Bassalo \t RM-558710 ")
        elif opcao == '5':
            print("\n==================== // =====================\n")
            print("Saindo...")
            print("\n==================== // =====================\n")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()