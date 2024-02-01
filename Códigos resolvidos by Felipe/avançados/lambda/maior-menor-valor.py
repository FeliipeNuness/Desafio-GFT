"""Desenvolva um programa que apresente o maior e o menor
 valores da sequência ([54, 10, 29, 87, 7, 64])"""

numeros = [54, 10, 29, 87, 7, 64]

valor_maior = float('-inf')
valor_menor = float('inf')

for numero in numeros:
    if numero > valor_maior:
        valor_maior = numero
        if numero < valor_menor:
            valor_menor = numero

print(f"o maior valor da sequência fornecida é: {valor_maior}")
print(f"o menor valor da sequência fornecida é: {valor_menor}")