#                 Até 5 Kg               Acima de 5 Kg
# Morango         R$ 2,50 por Kg         R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg         R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor
# total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para
# ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
# adquiridas e escreva o valor a ser pago pelo cliente.

quant_quilo_morango = float(
    input('Digite a quantidade em quilograma(Kg) de morango: '))

quant_quilo_maca = float(
    input('Digite a quantidade em quilograma(Kg) de maçã: '))

quant_quilo_total = quant_quilo_morango + quant_quilo_maca

# Formula para a quantidade até 5kg e acima de 5kg de morango
preco_morango_ate5 = quant_quilo_morango * 2.5
preco_morango_acima5 = quant_quilo_morango * 2.2

# Formula para a quantidade até 5kg e acima de 5kg de maçã
preco_maca_ate5 = quant_quilo_maca * 1.8
preco_maca_acima5 = quant_quilo_maca * 1.5

if quant_quilo_morango <= 5:
    preco_morango = preco_morango_ate5
else:
    preco_morango = preco_morango_acima5

if quant_quilo_maca <= 5:
    preco_maca = preco_maca_ate5
else:
    preco_maca = preco_maca_acima5

preco_total = preco_morango + preco_maca

if preco_total > 25 or quant_quilo_total > 8:
    print(f'Valor sem desconto: {preco_total}\
          \nValor do desconto: {preco_total * 0.1:.2f}\
          \nValor total com desconto: {preco_total - (preco_total * 0.1):.2f}')
else:
    print(f'Valor total: {preco_total}')
