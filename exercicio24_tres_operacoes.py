# Faça um Programa que leia 2 números e em seguida pergunte ao usuário
# qual operação ele deseja realizar. O resultado da operação deve
# ser acompanhado de uma frase que diga se o número é:


operacao = input('Escolhe entre essas operações:\
      \na - Par ou Ímpar\
      \nb - Positivo ou Negativo\
      \nc - Inteiro ou Decimal\
      \nDigite uma letra: ')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite mais um: '))

if operacao == 'a' or operacao == 'A':
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(f'Os números: {num1} e {num2} são pares')

    elif num1 % 2 != 0 and num2 % 2 != 0:
        print(f'Os números: {num1} e {num2} são ímpares')

    elif num1 % 2 == 0 and num2 % 2 != 0:
        print(f'O número {num1} é par e o número {num2} é ímpar')

    else:
        print(f'O número {num1} é ímpar e o número {num2} é par')

elif operacao == 'b' or operacao == 'B':
    if num1 > 0 and num2 > 0:
        print(f'Os números: {num1} e {num2} são positivos')

    elif num1 < 0 and num2 < 0:
        print(f'Os números: {num1} e {num2} são negativos')

    elif num1 > 0 and num2 < 0:
        print(f'O número {num1} é positivo e o número {num2} é negativo')

    else:
        print(f'O número {num1} é negativo e o número {num2} é positivo')

elif operacao == 'c' or operacao == 'C':
    if round(num1) == num1 and round(num2) == num2:
        print(f'Os números: {num1} e {num2} são inteiros')

    elif round(num1) != num1 and round(num2) != num2:
        print(f'Os números: {num1} e {num2} são decimais')

    elif round(num1) != num1 and round(num2) == num2:
        print(f'O número {num1} é decimal e o número {num2} é inteiro')

    else:
        print(f'O número {num1} é inteiro e o número {num2} é decimal')

else:
    print('Escolha inválida')
