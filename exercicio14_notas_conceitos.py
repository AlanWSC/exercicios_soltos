# Faça um programa que lê as duas notas parciais obtidas por um aluno numa
# disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media_nota = (nota1 + nota2)/2

if media_nota > 9 and media_nota <= 10:
    print(f'A sua primeira nota foi: {nota1}\
          \nA sua segunda nota foi: {nota2}\
          \nSua média geral foi: {media_nota}\
          \nSeu conceito final foi: A\
          \nParabéns! Você foi aprovado!')

elif media_nota > 7.5 and media_nota <= 9:
    print(f'A sua primeira nota foi: {nota1}\
          \nA sua segunda nota foi: {nota2}\
          \nSua média geral foi: {media_nota}\
          \nSeu conceito final foi: B\
          \nParabéns! Você foi aprovado!')

elif media_nota > 6 and media_nota <= 7.5:
    print(f'A sua primeira nota foi: {nota1}\
          \nA sua segunda nota foi: {nota2}\
          \nSua média geral foi: {media_nota}\
          \nSeu conceito final foi: C\
          \nParabéns! Você foi aprovado!')

elif media_nota > 4 and media_nota <= 6:
    print(f'A sua primeira nota foi: {nota1}\
          \nA sua segunda nota foi: {nota2}\
          \nSua média geral foi: {media_nota}\
          \nSeu conceito final foi: D\
          \nInfelizmente, você foi reprovado')

elif media_nota > 0 and media_nota <= 4:
    print(f'A sua primeira nota foi: {nota1}\
          \nA sua segunda nota foi: {nota2}\
          \nSua média geral foi: {media_nota}\
          \nSeu conceito final foi: E\
          \nInfelizmente, você foi reprovado')
