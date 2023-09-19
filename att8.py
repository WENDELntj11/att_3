numero_aleatorio = random.randint(1, 100)

# Contador de tentativas
tentativas = 0

print("Bem-Vindo ao jogo onde você adivinha o número!")
print("Tente adivinhar o número de 1 a 100.")

while True:
    tentativa = int(input("Digite um número:"))
    tentativas += 1

    if tentativa == numero_aleatorio:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break
    elif tentativa < numero_aleatorio:
        print("Você errou! Tente um número maior.")
    else:
        print("Você errou! lula! Tente um número menor.")
