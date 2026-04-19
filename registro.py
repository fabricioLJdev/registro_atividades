# Projeto: registro de atividades
# Descrição: Este programa permite que o usuário registre, visualize,
# busque e exclua atividades ou notas em um arquivo de texto.

NOME_ARQUIVO = "atividade.txt"

# adicionar atividade
def adicionar_atividade():
    atividade = input("Digite a atividade que deseja salvar no arquivo: ")

    with open(NOME_ARQUIVO, "a") as arquivo:
        arquivo.write(atividade + "\n")
    print("Atividade registrada com sucesso!")

# visualizar todas atividades
def visualizar_atividades():
    try:
        with open(NOME_ARQUIVO, "r") as arquivo:
            atividades = arquivo.readlines()

            if atividades:

                print("=== Atividades Registradas ===")
                for i, atividade in enumerate(atividades, start=1):
                    print(f"{i}. {atividade}")

            else:
                print("Você não adicionou nenhuma atividade")

    except FileNotFoundError:
        print("Nenhum arquivo foi encontrado")

# Buscar atividades
def buscar_atividades():
    try:
        termo = input("Digite o termo para buscar: ")

        with open(NOME_ARQUIVO, "r") as arquivo:
            atividades = arquivo.readlines()

        resultados = [atividade.strip() for atividade in atividades if termo.lower() in atividade.lower()]

        if resultados:
            print("=== Atividades Registradas ===")
            
            for i, resultado in enumerate(resultados, start=1):
                print(f"{i}. {resultado}")
        
        else:
            print(f"Nenhuma atividade encontrada para o termo {termo}")

    except FileNotFoundError:
        print("Nenhuma atividade registrada ainda")

def excluir_atividades():
    visualizar_atividades()
    try:
        with open(NOME_ARQUIVO, "r") as arquivo:
            atividades = arquivo.readlines()

        if atividades:
            indice = int(input("Digite o número da atividade que deseja excluir: "))

            if 1 <= indice <= len(atividades):
                atividade_excluida = atividades.pop(indice - 1) # metodo pop é passado o numero do indice
                
                with open(NOME_ARQUIVO, "w") as arquivo:
                    arquivo.writelines(atividades)

                print(f"Atividade {atividade_excluida.strip()} excluída com sucesso")

            else:
                print("Número inválido. Nenuma atividade foi excluída.")

        else:
            print("Nunhuma atividade encontrada")
    except FileNotFoundError:
        print("Nenhum arquivo foi encontrado")


def menu_principal():
    while True:
        print("=== Menu Principal ===")
        print("1. Adicionar uma nova atividade")
        print("2. visualizar todas as atividades")
        print("3. Buscar uma atividade")
        print("4. Excluir uma atividade")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_atividade()
        elif opcao == "2":
            visualizar_atividades()
        elif opcao == "3":
            buscar_atividades()
        elif opcao == "4":
            excluir_atividades()
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    menu_principal()
