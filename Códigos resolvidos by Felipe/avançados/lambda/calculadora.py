"""Desenvolva uma calculadora rudimentar onde o usuário deve informar: 
qual operação ele deseja realizar, quais os valores para a realização do cálculo 
(apenas dois valores)
 e o resultado da operação - Código by Felipe"""

def soma (n1, n2):
    return n1 + n2

def subtracao (n1, n2):
    return n1 - n2

def mutiplicacao (n1,n2):
    return n1 * n2

def divisao (n1, n2):
    if n2 == 0:
        return "Erro! Não existe divisão por zero"
    return n1 / n2

operacao = input("Digite qual operação deseja realizar(+, -, *, /):")

valor1 = float(input("Digite o primero valor:"))
valor2 = float(input("DIgite o segundo valor:"))

if operacao == '+':
    resultado = soma(valor1,valor2)
elif operacao == '-':
    resultado = subtracao(valor1,valor2)
elif operacao == '*':
    resultado = mutiplicacao(valor1,valor2)
elif operacao == '/':
    resultado = divisao(valor1,valor2)
else:
    resultado = "Operação invalida"

print(f"Resultado da operação {valor1} {operacao} {valor2} é: {resultado}")



    
