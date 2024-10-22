from menu import menu

def main():

    while True:
        opcao = menu()

        if opcao == '1':
            print("Opção produtos selecionada. \n")
        elif opcao == '2':
            print("Opção fornecedores selecionada. \n")
        elif opcao == '3':
            print("Opção pedidos selecionada. \n")
        elif opcao == '4':
            print("Opção Participantes selecionada. \n")
            print("\n\tKauã Fermino Zipf \t RM-558957")
            print("\n\tCaetano Penafiel \t RM-557984")
            print("\n\tVictor Egidio Lira \t RM-556653")
            print("\n\tDiego Bassalo \t RM-558710")
        elif opcao == '5':
            print("Opção de saida selecionada. \n")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()