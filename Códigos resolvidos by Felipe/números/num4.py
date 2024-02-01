"""Desenvolva um programa que leia um número inteiro qualquer e
 que informe se este número é par ou impar - Código by Felipe"""


numero = int(input("Digite um número inteiro:"))

if numero %2 == 0:
    print(f"{numero}, o número é par")
else:
    print(f"{numero}, o número é ímpar")