# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
# e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo
# grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

# Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa;

import sys

print('Calculando equação de segundo grau')

a = float(input('Digite o valor de (a): '))

if a == 0:
    print('A equação não é do 2º grau\
          \nO programa será finalizado')
    sys.exit()

b = float(input('Digite o valor de (b): '))
c = float(input('Digite o valor de (c): '))

calc_delta = b**2 - 4 * a * c

if calc_delta < 0:
    print(
        f'O resultado do delta é: {calc_delta}. \
        A equação não possui raizes reais')

elif calc_delta == 0:
    print(
        f'O resultado do delta é: {calc_delta},\
        portanto as duas raizes são iguais.')

elif calc_delta > 0:
    print(
        f'O resultado do delta é: {calc_delta}. \
        Portanto, possui duas raizes diferentes')
