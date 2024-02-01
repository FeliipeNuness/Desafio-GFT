"""Desenvolva um programa que apresente a soma dos valores
 pares e dos valores ímpares da sequência ([21, 5, 34, 8, 16, 7, 3]) """

numeros = [21, 5, 34, 8, 16, 7, 3]

soma_par = 0
soma_impar = 0 

for numero in numeros:
    if numero % 2 == 0:
        soma_par += numero
    else:
        soma_impar += numero

print(f"soma dos valores pares:{soma_par}")
print(f"soma dos valores ímpares:{soma_impar}")