import random

def sim_nao_talvez():
    pergunta = input("Insira sua pergunta: ")
    resposta = random.choice(["Sim", "Não", "Talvez"])
    print("Resposta:", resposta)

sim_nao_talvez()