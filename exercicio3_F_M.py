# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme  letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra_fm = input('Digite uma letra: ')

if letra_fm == 'f' or letra_fm == 'F':
    print(f'{letra_fm} é Feminino!')

elif letra_fm == 'm' or letra_fm == 'M':
    print(f'{letra_fm} é Masculino!')

else:
    print(f'{letra_fm} é desconhecido!')
