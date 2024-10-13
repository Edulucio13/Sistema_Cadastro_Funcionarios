'''
Descrição:
Você foi contratado para desenvolver um sistema básico de gerenciamento de funcionários para uma pequena empresa. O sistema deve ser capaz de receber e armazenar informações sobre os funcionários e realizar operações básicas de manipulação desses dados.

Requisitos:
Utilize a função input() -  realizar um cadastro coletando dados do usuário, como nome, cidade e estado em que reside, idade, escolaridade, cargo e salário.
 
Funcionalidades do Sistema:
O sistema deve oferecer as seguintes funcionalidades:
Adicionar um novo funcionário ao sistema, solicitando informações como nome, cargo, salário, e-mail, etc.
Atualizar as informações de um funcionário existente com base em um identificador único (como um número de identificação ou nome). Exibir informações de um funcionário específico.
'''
# Lista para armazenar os funcionários
funcionarios = [] # iniciando a lista de funcionários
func_id_proximo = 1 #iniciando o contador do ID do funcionário

# iniciando o menu de opções:
while True:
    print("\nSistema de Controle de Funcionários\n")
    print("1. Adicionar Funcionário")
    print("2. Atualizar Funcionário")
    print("3. Exibir Funcionário")
    print("4. Listar Funcionários")
    print("5. Remover Funcionário")
    print("6. Sair")
    opcao = input("\nEscolha uma opção: ")

    # opção 1 - Adicionar funcionários    
    if opcao == '1':
        nome_1 = input("Nome: ")
        nome = nome_1.upper()
        # Verificação se o funcionário já existe
        if any(func['Nome'] == nome for func in funcionarios):
            print("\nFuncionário já existe.\n")
        else:
            cidade_1 = input("Cidade: ")
            cidade = cidade_1.upper()
            estado_1 = input("Estado: ")
            estado = estado_1.upper()
            # Verificação se a idade é um número inteiro
            while True:
                try:
                    idade = int(input("Idade: "))
                    break
                except ValueError:
                    print("\nPor favor, digite um número inteiro válido para a idade.\n")
            
            educacao_1 = input("Escolaridade: ")
            educacao = educacao_1.upper()
            cargo_1 = input("Cargo: ")
            cargo = cargo_1.upper()
             # Verificação se o salário é um float
            while True:
                try:
                    salario = float(input("Salário: "))
                    break
                except ValueError:
                    print("\nPor favor, digite um número válido para o salário.\n")
            
            email_1 = input("E-mail: ")
            email = email_1.lower()


            # Criando dicionário para armazenar os dados do funcionário
            funcionario = {
                'ID': func_id_proximo,
                'Nome': nome,
                'Cidade': cidade,
                'Estado': estado,
                'Idade': idade,
                'Escolaridade': educacao,
                'Cargo': cargo,
                'Salário': salario,
                'E-mail': email
            }
            funcionarios.append(funcionario) # Adiciona o funcionário
            func_id_proximo += 1  # Incrementa o ID para o próximo funcionário
            print("\nFuncionário adicionado com sucesso!\n")
    
    # opção 2 - Atualizar funcionários
    elif opcao == '2':
        # Verificação se o número do ID é inteiro
        while True:
            try:
                func_id = int(input("ID do Funcionário para atualização: "))
                break
            except ValueError:
                print("\nPor favor, digite um número inteiro válido para o ID.\n")
        # Percorrendo o ID na lista
        for func in funcionarios:
            if func['ID'] == func_id:
                func['Nome'] = input("Nome: ")
                func['Cidade'] = input("Cidade: ")
                func['Estado'] = input("Estado: ")
                
                 # Verificação se a idade é um número inteiro
                while True:
                    try:
                        func['Idade'] = int(input("Idade: "))
                        break
                    except ValueError:
                        print("\nPor favor, digite um número inteiro válido para a idade.\n")
                
                func['Escolaridade'] = input("Escolaridade: ")
                func['Cargo'] = input("Cargo: ")
                
                # Verificação se o salário é um float
                while True:
                    try:
                        func['Salário'] = float(input("Salário: "))
                        break
                    except ValueError:
                        print("\nPor favor, digite um número válido para o salário.\n")
                
                func['E-mail'] = input("E-mail: ")
                print("\nFuncionário atualizado com sucesso!\n")
                break
        else:
            print("\nFuncionário não encontrado.\n")
    
    # opção 3 - Exibir funcionários
    elif opcao == '3':
        # Verificação se o número do ID é inteiro
        while True:
            try:
                func_id = int(input("ID do Funcionário para exibição: "))
                break
            except ValueError:
                print("\nPor favor, digite um número inteiro válido para o ID.\n")
        # Percorrendo o ID na lista
        for func in funcionarios:
            if func['ID'] == func_id:
                print(f"\nNome: {func['Nome']}, Cidade: {func['Cidade']}, Estado: {func['Estado']}, Idade: {func['Idade']}, Escolaridade: {func['Escolaridade']}, Cargo: {func['Cargo']}, Salário: {func['Salário']}, E-mail: {func['E-mail']}\n")
                break
        else:
            print("\nFuncionário não encontrado.\n")
    
    # opção 4 - Listar funcionários
    elif opcao == '4':
        # Verificação se existem funcionários cadastrados
        if not funcionarios:
            print("\nNenhum funcionário cadastrado.\n")
        else:
            # Percorrendo os IDs na lista
            for func in funcionarios:
                print(f"\nID: {func['ID']}, Nome: {func['Nome']}, Cargo: {func['Cargo']}\n")
    
    # opção 5 - Remover funcionários
    elif opcao == '5':
        # Verificação se o número do ID é inteiro
        while True:
            try:
                func_id = int(input("ID do Funcionário para remoção: "))
                break
            except ValueError:
                print("\nPor favor, digite um número inteiro válido para o ID.\n")
        # Percorrendo o ID na lista
        for func in funcionarios:
            if func['ID'] == func_id:
                funcionarios.remove(func) # Remoção do ID
                print("\nFuncionário removido com sucesso!\n")
                break
        else:
            print("\nFuncionário não encontrado.\n")
    
    # opção 6 - Sair do menu
    elif opcao == '6':
        print("\nSaindo...\n")
        break
    # Verificação da opção escolhida. Se for diferente das opções, informa mensagem abaixo e retorna]]
    else:
        print("\nOpção inválida, por favor tente novamente.\n")
