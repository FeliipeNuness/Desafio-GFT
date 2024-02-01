""""Desenvolva um programa que armazene quatro notas em uma lista e que apresente:
 a média final, a maior nota e a menor nota. Código by Felipe"""

notas = []

for i in range(4):
    nota = float(input(f"Digite sua {i + 1}ª nota:"))
    notas.append(nota)

media = sum(notas) / len(notas)

maiorNota = max(notas)
menorNota = min(notas)

print("Sua media final foi: {}, sua maior nota foi: {}, e sua menor nota foi {}".format(media, maiorNota, menorNota))
