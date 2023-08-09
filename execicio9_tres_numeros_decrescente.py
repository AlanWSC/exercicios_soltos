# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 < num2 and num2 < num3:
    print(f'Em ordem descrescente fica assim: {num3},{num2},{num1}')

elif num2 < num1 and num1 < num3:
    print(f'Em ordem descrescente fica assim: {num3},{num1},{num2}')

elif num3 < num2 and num2 < num1:
    print(f'Em ordem descrescente fica assim: {num1},{num2},{num3}')

elif num1 < num3 and num3 < num2:
    print(f'Em ordem descrescente fica assim: {num2},{num3},{num1}')

elif num2 < num3 and num3 < num1:
    print(f'Em ordem descrescente fica assim: {num1},{num3},{num2}')

elif num3 < num1 and num1 < num2:
    print(f'Em ordem descrescente fica assim: {num2},{num1},{num3}')

else:
    print('Números iguais!')
