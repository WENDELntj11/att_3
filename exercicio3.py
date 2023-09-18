def  e_multiplo_de_5(numero):
    if numero % 5 == 0:
       return True
    else:
        return False
numero = int(input("Digite um numero:"))
print(e_multiplo_de_5(numero))