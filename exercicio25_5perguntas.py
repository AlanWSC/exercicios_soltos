# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são: O programa deve no final emitir uma classificação
# sobre a participação da pessoa no crime. Se a pessoa responder positivamente
# a 2 questões ela deve ser classificada como "Suspeita", entre
# 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".


print('Responda as 5 perguntas apenas com "S" ou "N"')

n_respostas = 0

pergunta1 = input('Telefonou para a vítima?')

if pergunta1 == 'S' or pergunta1 == 's':
    n_respostas += 1

pergunta2 = input('Esteve no local do crime?')

if pergunta2 == 'S' or pergunta2 == 's':
    n_respostas += 1

pergunta3 = input('Mora perto da vítima?')

if pergunta3 == 'S' or pergunta3 == 's':
    n_respostas += 1

pergunta4 = input('Devia para a vítima?')

if pergunta4 == 'S' or pergunta4 == 's':
    n_respostas += 1

pergunta5 = input('Já trabalhou com a vítima?')

if pergunta5 == 'S' or pergunta5 == 's':
    n_respostas += 1


if n_respostas == 2:
    print('Você é considerado suspeito')

elif n_respostas >= 3 and n_respostas <= 4:
    print('Você é considerado cumplice')

elif n_respostas == 5:
    print('Você é considerado assassino')

elif n_respostas <= 1:
    print('Você é considerado inocente')
