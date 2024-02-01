"""Desenvolva um programa que leia quatro notas e que apresente a média final"""

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota:"))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Sua média final é: {media:.2f}")