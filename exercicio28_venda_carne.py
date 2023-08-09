#                     Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas
# um dos tipos de carne da promoção, porém não há limites para a quantidade
# de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e
# quantidade de carne, preço total, tipo de pagamento,
# valor do desconto e valor a pagar.

from random import randint as rand

numero_carne = input('1 - Filé Duplo\
                     \n2 - Alcatra\
                     \n3 - Picanha\
                     \nDigite o número da carne escolhida: ')

if numero_carne == '1':
    quant_quilo_file = int(input('\nVocê escolheu Filé Duplo.\
    \nAgora, digite quantos quilogramas(Kg) deseja comprar: '))

    if quant_quilo_file <= 5:
        preco_file = quant_quilo_file * 4.9
    else:
        preco_file = quant_quilo_file * 5.8

elif numero_carne == '2':
    quant_quilo_alcatra = int(input('\nVocê escolheu Alcatra.\
    \nAgora, digite quantos quilogramas(Kg) deseja comprar: '))

    if quant_quilo_alcatra <= 5:
        preco_alcatra = quant_quilo_alcatra * 5.9
    else:
        preco_alcatra = quant_quilo_alcatra * 6.8

elif numero_carne == '3':
    quant_quilo_picanha = int(input('\nVocê escolheu Alcatra.\
    \nAgora, digite quantos quilogramas(Kg) deseja comprar: '))

    if quant_quilo_picanha <= 5:
        preco_picanha = quant_quilo_picanha * 6.9
    else:
        preco_picanha = quant_quilo_picanha * 7.8

pagamento = input(f'\nDeseja pagar no cartão?\
                  \nS ou s = Sim\
                  \nN ou n = Não\
\nOBS: Pagando com o cartão da loja terá 5% de desconto no total da compra\n')

if pagamento == 'S' or pagamento == 's':
    if numero_carne == '1':
        print(f'\nNúmero do cupom fiscal: {rand(1,2500)}\
              \nSua escolha de compra foi: {numero_carne} - Filé Duplo\
              \nA quantidade em quilograma(Kg): {quant_quilo_file} Kg\
              \nPreço total(Sem desconto): {preco_file:.2f}\
              \nPagamento escolhido: Cartão da loja\
              \nValor total do desconto: {preco_file * 0.05:.2f}\
              \nPreço total(Com desconto): {preco_file - (preco_file * 0.05):.2f}\
              \nValor a pagar: {preco_file - (preco_file * 0.05):.2f}')
