def exibir_tarefas(tarefas):
    print('Lista das Tarefas:')
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else 'Pendente'
        print(f"{i}. [{status}] {tarefa["descricao"]}")
def remover_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        del tarefas[indice]
    else:
        print("Índice inválido.")

# Função para salvar a lista de tarefas em um arquivo
def salvar_tarefas_arquivo(tarefas, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa['descricao']},{tarefa['concluida']}\n")

# Função para carregar a lista de tarefas de um arquivo
def carregar_tarefas_arquivo(nome_arquivo):
    tarefas = []
 if os.path.exists(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
     for linha in arquivo:
                descricao, concluida_str = linha.strip().split(",")
                concluida = concluida_str == "True"
                tarefas.append({"descricao": descricao, "concluida": concluida})
return tarefas

# Nome do arquivo para armazenar as tarefas
nome_arquivo = "tarefas.txt"

# Carregar as tarefas do arquivo (se existir)
tarefas = carregar_tarefas_arquivo(nome_arquivo)

while True:
    print("\nOpções:")
    print("1. Exibir Tarefas")
    print("2. Adicionar Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        exibir_tarefas(tarefas)
     elif escolha == "2":
        descricao = input("Digite uma descrição da tarefa: ")
        adicionar_tarefa(tarefas, descricao)
        salvar_tarefas_arquivo(tarefas, nome_arquivo)
        print("Tarefa adicionada com sucesso.")
     elif escolha == "3":
        exibir_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        marcar_tarefa_concluida(tarefas, indice)
        salvar_tarefas_arquivo(tarefas, nome_arquivo)
        print("Tarefa marcada como concluída.")
     elif escolha == "4":
        exibir_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        remover_tarefa(tarefas, indice)
        salvar_tarefas_arquivo(tarefas, nome_arquivo)
        print("Tarefa removida com sucesso.")
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
