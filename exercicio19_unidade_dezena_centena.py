# Faça um Programa que leia um número inteiro menor que 1000
# e imprima a quantidade de centenas, dezenas e unidades do mesmo

'''
numero = int(input('Digite um numero inteiro positivo: '))

# Extraindo a unidade
unidade = numero % 10
print(unidade)

#Eliminando a unidade de nosso número
numero = (numero - unidade)/10
print(numero)

# Extraindo a dezena
dezena = numero % 10
print(dezena)

#Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero

# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)
print(centena, 'centena(s),', dezena, 'dezena(s) e', unidade, 'unidade(s)')
'''

numero = int(input('Digite um número: '))

if numero > 999:
    print('O número deve ser menor que 1000')

else:

    num = str(numero)

    if numero <= 9:
        print(f'Temos {format(num[0])} unidade(s)')

    elif numero >= 10 and numero <= 99:
        print(
            f'Temos {format(num[0])} dezena(s) e {format(num[1])} unidade(s)')

    elif numero >= 100 and numero <= 999:
        print(
            f'Temos {format(num[0])} centena(s), {format(num[1])} dezena(s) e {format(num[2])} unidade(s)')
