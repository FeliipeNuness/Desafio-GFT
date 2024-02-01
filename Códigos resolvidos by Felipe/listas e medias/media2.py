"""Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final.
 Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO",
 caso contrário, armazenar a nota da prova final e recalcular a média.
   Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO",
 caso contrário, apresentar a mensagem "REPROVADO - Código by Felipe"""

notas = []

for i in range(4):
    nota = float(input(f"Digite sua {i + 1}ª nota:"))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    print(f"Aprovado! Média final: {media:.2f}")
else:
    prova_final = float(input("Digite a nota da prova final:"))

nova_media = (sum(notas) + prova_final) / (len(notas) + 1)

if nova_media >= 5:
    print(f"aprovado na prova final! sua nova media é: {nova_media:.2f}")
else:
    print(f"reprovado! sua nova media é: {nova_media:.2f}")
    