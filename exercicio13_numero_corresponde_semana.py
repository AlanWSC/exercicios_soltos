# Faça um Programa que leia um número e exiba
# o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.)
# , se digitar outro valor deve aparecer valor inválido.


numero_semana = input('Digite um número para descobrir o dia da semana: ')

if numero_semana == '1':
    print(f'O numero {numero_semana} == Domingo')
elif numero_semana == '2':
    print(f'O numero {numero_semana} == Segunda')
elif numero_semana == '3':
    print(f'O numero {numero_semana} == Terça')
elif numero_semana == '4':
    print(f'O numero {numero_semana} == Quarta')
elif numero_semana == '5':
    print(f'O numero {numero_semana} == Quinta')
elif numero_semana == '6':
    print(f'O numero {numero_semana} == Sexta')
elif numero_semana == '7':
    print(f'O numero {numero_semana} == Sábado')
else:
    print('Valor inválido')
