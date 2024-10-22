from menu import menu, menu_produtos, menu_fornecedor, menu_pedidos
from servicos import cadastrar_produto, exibir_produtos, cadastrar_fornecedor, exibir_fornecedores, cadastrar_pedido, exibir_pedidos

def main():

    while True:
        opcao = menu()

        if opcao == '1':
            print("Opção produtos selecionada. \n")
            opcao_produtos = menu_produtos()
            if opcao_produtos == "1":
                cadastrar_produto()
            elif opcao_produtos == "2":
                exibir_produtos()
            elif opcao_produtos == "3":
                print("Saindo...")
                break
            else: 
                print("Opção inválida.")
        elif opcao == '2':
            print("Opção fornecedores selecionada. \n")
            opcao_produtos = menu_fornecedor()
            if opcao_produtos == "1":
                cadastrar_fornecedor()
            elif opcao_produtos == "2":
                exibir_fornecedores()
            elif opcao_produtos == "3":
                print("Saindo...")
                break
            else: 
                print("Opção inválida.")
        elif opcao == '3':
            print("Opção pedidos selecionada. \n")
            opcao_produtos = menu_pedidos()
            if opcao_produtos == "1":
                cadastrar_pedido()
            elif opcao_produtos == "2":
                exibir_pedidos()
            elif opcao_produtos == "3":
                print("Saindo...")
                break
            else: 
                print("Opção inválida.")
        elif opcao == '4':
            print("Opção Participantes selecionada. \n")
            print("\n\tKauã Fermino Zipf \t RM-558957")
            print("\n\tCaetano Penafiel \t RM-557984")
            print("\n\tVictor Egidio Lira \t RM-556653")
            print("\n\tDiego Bassalo \t RM-558710")
        elif opcao == '5':
            print("Opção de saida selecionada. \n")
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()