# Projeto: registro de atividades
# Descrição: Este programa permite que o usuário registre, visualize,
# busque e exclua atividades ou notas em um arquivo de texto.

NOME_ARQUIVO = "atividade.txt"

# adicionar atividade
def adicionar_atividade():
    atividade = input("Digite a atividade que deseja adicionar: ")

    with open(NOME_ARQUIVO, "a") as arquivo:
        arquivo.write(atividade + "\n")

        print("Atividade foi adicionada")

# visualizar todas atividades
def visualizar_atividades():
    try:
        with open(NOME_ARQUIVO, "r") as arquivo:
            atividades = arquivo.readlines()

            if atividades:
                dados = [atividade.strip() for atividade in atividades if atividade.strip()]

                print(dados)

            else:
                print("Você não adicionou nenhuma atividade")

    except FileNotFoundError:
        print("Nenhum arquivo foi encontrado")
def menu_principal():
    while True:
        print("=== Menu Principal ===")
        print("1. Adicionar uma nova atividade")
        print("2. visualizar todas as atividades")
        print("3. Buscar um atividade")
        print("4. Excluir uma atividade")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_atividade()
        elif opcao == "2":
            visualizar_atividades()
        elif opcao == "3":
            print("opcao 3")
        elif opcao == "4":
            print("opcao 4")
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    menu_principal()
