print("Bem vindo a Empresa de Endrigo Rafael Pusch")
print("-" * 60)

#==== Variaveis para atribuiçao global no programa ====
lista_funcionarios = []
id_global = 4966480


def cadastrar_funcionario(id):
    print("-" * 60)
    print("-------------- MENU CADASTRAR FUNCIONARIO ------------------")
    id = id_global + 1
    print("Id do Funcionario: ", id)
    nome = input("Por favor entre com o nome do Funcionario: ")
    setor = input("Por favor entre com o setor do Funcionario: ")
    salario = float(input("Por favor entre com o salario do Funcionario: "))
    print("-" * 60)

    #===Dicionario===
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_funcionarios.append(funcionario.copy())


def consultar_funcionarios():
    while True:
        print("-" * 60)
        opcao = int(input("-------------- MENU CONSULTAR FUNCIONARIO ------------------\n"
                          "Escolha a opçao desejada:\n"
                          "1 - Consultar Todos os Funcionarios\n"
                          "2 - Consultar Funcionarios por id\n"
                          "3 - Consultar Funcionario(s) por setor\n"
                          "4 - Retornar\n"
                          ""))

        if opcao == 1:
            print("-" * 40)
            for funcionario in lista_funcionarios:
                print(f"id: {funcionario['id']}\n"
                      f"nome: {funcionario['nome']}\n"
                      f"setor: {funcionario['setor']}\n"
                      f"salario: {funcionario['salario']}\n")
        elif opcao == 2:
            id_consulta = int(input("Informe o ID do funcionario: "))
            print("-" * 40)
            for funcionario in lista_funcionarios:
                if funcionario["id"] == id_consulta:
                    print(f"id: {funcionario['id']}\n"
                          f"nome: {funcionario['nome']}\n"
                          f"setor: {funcionario['setor']}\n"
                          f"salario: {funcionario['salario']}\n")
                    print("-" * 40)
                    break
            else:
                print("Funcionario nao encontrado.")
        elif opcao == 3:
            setor_consulta = input("Informe o setor do funcionario: ")
            print("-" * 40)
            for funcionario in lista_funcionarios:
                if funcionario["setor"] == setor_consulta:
                    print(f"id: {funcionario['id']}\n"
                          f"nome: {funcionario['nome']}\n"
                          f"setor: {funcionario['setor']}\n"
                          f"salario: {funcionario['salario']}\n")
                    print("-" * 40)
        elif opcao == 4:
            return
        else:
            print("Opçao invalida.")


def remover_funcionario():
    while True:
        id_remover = int(input("Informe o ID do funcionario: "))
        for funcionario in lista_funcionarios:
            if funcionario["id"] == id_remover:
                lista_funcionarios.remove(funcionario)
                print("Funcionario removido.")
                return
        else:
            print("Id nao encontrado.")


while True:
    opcao = int(input("-------------------- MENU PRINCIPAL ------------------------\n"
                      "Escolha a opçao desejada:\n"
                      "1 - Cadastrar Funcionario\n"
                      "2 - Consultar Funcionarios\n"
                      "3 - Remover Funcionario\n"
                      "4 - Sair\n"))

    if opcao == 1:
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == 2:
        consultar_funcionarios()
    elif opcao == 3:
        remover_funcionario()
    elif opcao == 4:
        print("Encerrando Programa.")
        break
    else:
        print("Opçao invalida.")
