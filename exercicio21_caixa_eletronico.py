# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
# usuário a valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com
# a quantidade de notas existentes na máquina

valor_saque = float(input('Digite o valor de saque: '))

if valor_saque < 10 or valor_saque > 600:
    print('Valor inválido!\
          \nDigite um valor maior que 10 ou menor que 600.')

else:
    cem = valor_saque // 100
    # Pegamos a centena com uma divisão inteira
    print(f'Aqui serão duas notas: {cem}')
    valor_saque -= cem * 100  # Subtraímos as centenas retiradas do valor total
    print(valor_saque)
    cinquenta = valor_saque // 50  # Idem para as outras coisas
    valor_saque -= cinquenta * 50
    dez = valor_saque // 10
    valor_saque -= dez * 10
    cinco = valor_saque // 5
    valor_saque -= cinco * 5
    um = valor_saque  # Depois de subtrair as de cinco só sobram as de um
    print(um)
    if cem > 0:
        print(f"{cem} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco} nota(s) de cinco")
    if um > 0:
        print(f"{um} nota(s) de um")
