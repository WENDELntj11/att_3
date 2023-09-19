def fatorial(n):
    if n < 0:
        raise ValueError("Não foi possível calcular o fatorial de um número negativo")
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

try:
    numero = int(input("Insira algum número para calcular o fatorial: "))
    resultado = fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
except ValueError as e:
    print(e)
