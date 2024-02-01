"""Desenvolva um programa que leia um número inteiro qualquer e que apresete o número informado,
 seguido do seu antecessor e do seu sucessor - código by Felipe"""

numero = int(input("Digite um número inteiro:"))

antecessor = numero - 1
sucessor = numero + 1

print("O número infomado foi:{} seu antecessor é {}, seu sucessor é: {}".format(numero, antecessor, sucessor))