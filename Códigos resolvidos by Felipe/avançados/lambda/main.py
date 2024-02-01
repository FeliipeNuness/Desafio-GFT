"""Desenvolva um programa que leia o seu nome completo e que apresente somente
 o seu primeiro e último nome - Código by Felipe"""

nome_completo = input("Digite seu nome completo:")

parte_do_nome = nome_completo.split()

primero_nome = parte_do_nome[0]
ultimo_nome = parte_do_nome[-1]

print(f"Seu primeiro nome: {primero_nome}")
print(f"Seu segundo nome é:{ultimo_nome}")
