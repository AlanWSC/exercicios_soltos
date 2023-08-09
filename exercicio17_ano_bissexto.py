# Faça um Programa que peça um número correspondente a um determinado
# ano e em seguida informe se este ano é ou não bissexto.

ano_bissexto = int(input('Digite um ano: '))

if (ano_bissexto % 4) == 0:
    print(
        f'O ano que você digitou foi: {ano_bissexto}. Este foi ou será um ano bissexto.')
else:
    print('Este não é um ano bissexto.')
