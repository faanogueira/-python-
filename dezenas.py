# Solicita ao usuário que digite um número inteiro
numero_inteiro = int(input("Digite um número inteiro: "))

# Calcula o dígito das dezenas
digito_dezenas = (numero_inteiro // 10) % 10

# Imprime o dígito das dezenas
print(f"O dígito das dezenas é {digito_dezenas}")