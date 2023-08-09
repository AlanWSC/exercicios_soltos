# Faça um Programa que peça uma data no formato
# dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if dia > 31 or dia < 1:
    print('Digite um número de dia válido')

elif mes > 12 or mes < 1:
    print('Digite um número de mês válido')

elif ano < 1:
    print('Digite um ano válido')

else:
    print(f'Você digitou uma data válida: {dia}/{mes}/{ano}')
