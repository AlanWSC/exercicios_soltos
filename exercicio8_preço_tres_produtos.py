# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Digite o preço do primeiro produto: '))
produto2 = float(input('Digite o preço do segundo produto: '))
produto3 = float(input('Digite o preço do terceiro produto: '))

menor_preco = produto1

if produto2 < produto3 and produto2 < produto1:
    menor_preco = produto2

elif produto3 < produto2 and produto3 < produto1:
    menor_preco = produto3

print(f'Compre o produto com menor preço que é {menor_preco}')
