def gerar_senha(Comprimento, letras, numeros, caracteres_especiais):
    # Crie um lista com caracteres possíveis para cada categoria 
    caracteres = ""
    if letras:
        caracteres += string.ascii_letters
    if numeros:
        caracteres += string.digits
    if caracteres_especiais:
        caracteres += string.punctuation
    
    # Verifique se pelo menos uma categoria está habilitada 
    if not (letras or numeros or caracteres_especiais):
        return "Pelo menos uma Categoria deve está habilitada para gerar a senha."
    
    # Gere a senha aletória 
    senha = ''.join(random.choice(caracteres) for _ in range(Comprimento))
    return senha

# Solicitar as preferências do usuário
comprimento = int(input("Digite o comprimento da senha:"))
letras = input("Inseri letras na senha (sim/não): ").lower() == "sim"
numeros = input("Inseri números na senha (sim/não): ").lower() == "sim"
caracteres_especiais = input("Incluir caracteres especiais na senha (sim/não): ").lower() == "sim"

# Gerar a senha
senha_gerada = gerar_senha(comprimento, letras, numeros, caracteres_especiais)

# Exibir a senha gerada 
print(f'Senha gerada: "{senha_gerada}")
