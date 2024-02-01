"""Desenvolva um programa que converta todas as temperaturas desta lista 
em Celsius ([22.5, 40, 13, 29, 34]) para Fahrenheit - Código by Felipe"""

temperatura_celsius = [22.5, 40, 13, 29, 34]

def celsius_para_fahrenheit(celsius):
    return(celsius * 9/5) + 32

temperatura_fahrenheit = [celsius_para_fahrenheit(temp) for temp in temperatura_celsius]

print("Temperaturas em Celsius:", temperatura_celsius)
print("Temperaturas em Fahrenheit:", temperatura_fahrenheit)