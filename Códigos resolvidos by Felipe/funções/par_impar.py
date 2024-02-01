def impar_ou_par(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

try:
    numero = int(input("Digite um número inteiro:\n"))
    resultado = impar_ou_par(numero)
    print('Seu número digitado foi {} e ele é {}'.format(numero, resultado))

except ValueError:
    print("Por favor, digite um número inteiro que seja válido.")

""""Esse programa pede ao usuario um número e informa se o número digitado é ímpar ou par - Código by Felipe"""
