# As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


salario = float(input('Digite o valor do salário: '))

# print(f'O valor do salário {salario}')


if salario <= 280:
    aumento_porcertagem = (salario * 20)/100
    print(
        f'Seu salário antes do reajuste era: {salario}\
        \nFoi aplicado um aumento de 20%\
        \nO valor do aumento foi: {aumento_porcertagem}\
        \nSeu novo salário é: {salario + aumento_porcertagem}')

elif salario > 280 and salario <= 700:
    aumento_porcertagem = (salario * 15)/100
    print(
        f'Seu salário antes do reajuste era: {salario}\
        \nFoi aplicado um aumento de 15%\
        \nO valor do aumento foi: {aumento_porcertagem}\
        \nSeu novo salário é: {salario + aumento_porcertagem}')

elif salario > 700 and salario <= 1500:
    aumento_porcertagem = (salario * 10)/100
    print(
        f'Seu salário antes do reajuste era: {salario}\
        \nFoi aplicado um aumento de 10%\
        \nO valor do aumento foi: {aumento_porcertagem}\
        \nSeu novo salário é: {salario + aumento_porcertagem}')

elif salario > 1500:
    aumento_porcertagem = (salario * 5)/100
    print(
        f'Seu salário antes do reajuste era: {salario}\
        \nFoi aplicado um aumento de 5%\
        \nO valor do aumento foi: {aumento_porcertagem}\
        \nSeu novo salário é: {salario + aumento_porcertagem}')
