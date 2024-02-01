"""Desenvolva um programa que altere em tempo de execução a palavra 
Java pela palavra Python na frase Exercícios de Java - Código by Felipe"""


frase = input("Digite a frase contendo a palavra 'Java': ")

nova_frase = frase.replace('Java', 'Python')

print(f"A nova frase com a substituição é: {nova_frase}")
