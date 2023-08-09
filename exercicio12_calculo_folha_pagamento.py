# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme
# tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade
# de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o
# exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.


valor_hora = float(input('Digite o valor p/ hora trabalhada: '))
quant_hora = int(input('Digite o total de horas trabalhadas no mês: '))

salario_calculado = valor_hora * quant_hora
calc_fgts = (salario_calculado * 11)/100

if salario_calculado <= 900:
    print(f'Isento do Imposto de Renda\
          \nSalário bruto: {valor_hora} x {quant_hora} = {salario_calculado}\
          \nDesconto Imposto de Renda: 0\
          \nDesconto INSS: 0\
          \nFGTS(pago pela empresa): {calc_fgts}\
          \nTotal de descontos: 0\
          \nSalário líquido: {salario_calculado}')

elif salario_calculado > 900 and salario_calculado <= 1500:

    desc_ir = (salario_calculado * 5)/100

    desc_inss = (salario_calculado * 10)/100

    salario_liquido = salario_calculado - (desc_ir + desc_inss)

    print(f'Salário bruto: {valor_hora} x {quant_hora} = {salario_calculado}\
          \nDesconto Imposto de Renda: {desc_ir}\
          \nDesconto INSS: {desc_inss}\
          \nFGTS(pago pela empresa): {calc_fgts}\
          \nTotal de descontos: {desc_ir + desc_inss}\
          \nSalário líquido: {salario_liquido}')

elif salario_calculado > 1500 and salario_calculado <= 2500:
    desc_ir = (salario_calculado * 10)/100

    desc_inss = (salario_calculado * 10)/100

    salario_liquido = salario_calculado - (desc_ir + desc_inss)

    print(f'Salário bruto: {valor_hora} x {quant_hora} = {salario_calculado}\
          \nDesconto Imposto de Renda: {desc_ir}\
          \nDesconto INSS: {desc_inss}\
          \nFGTS(pago pela empresa): {calc_fgts}\
          \nTotal de descontos: {desc_ir + desc_inss}\
          \nSalário líquido: {salario_liquido}')

elif salario_calculado > 2500:
    desc_ir = (salario_calculado * 20)/100

    desc_inss = (salario_calculado * 10)/100

    salario_liquido = salario_calculado - (desc_ir + desc_inss)

    print(f'Salário bruto: {valor_hora} x {quant_hora} = {salario_calculado}\
          \nDesconto Imposto de Renda: {desc_ir}\
          \nDesconto INSS: {desc_inss}\
          \nFGTS(pago pela empresa): {calc_fgts}\
          \nTotal de descontos: {desc_ir + desc_inss}\
          \nSalário líquido: {salario_liquido}')
