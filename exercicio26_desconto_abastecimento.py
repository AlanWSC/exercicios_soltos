

opcao_abastecimento = input('Escolha uma opção para abastecer:\
                            \nA - Álcool\
                            \nG - Gasolina\
                            \nDigite: ')

litros_abastecimento = float(input('Digite quantos litros deseja abastecer: '))

if opcao_abastecimento == 'A' or opcao_abastecimento == 'a':
    if litros_abastecimento <= 20:
        desconto3_por_litro = 1.90 * 0.03
        total_desconto = litros_abastecimento * desconto3_por_litro
        total_sem_desconto = litros_abastecimento * 1.90
        total_com_desconto = total_sem_desconto - total_desconto
        print(f'Você irá pagar: {total_com_desconto}\
              \nPreço sem desconto: {total_sem_desconto}\
              \nValor do desconto: {total_desconto}')

    if litros_abastecimento > 20:
        desconto5_por_litro = 1.90 * 0.05
        total_desconto = litros_abastecimento * desconto5_por_litro
        total_sem_desconto = litros_abastecimento * 1.90
        total_com_desconto = total_sem_desconto - total_desconto
        print(f'Você irá pagar: {total_com_desconto}\
              \nPreço sem desconto: {total_sem_desconto}\
              \nValor do desconto: {total_desconto}')

elif opcao_abastecimento == 'G' or opcao_abastecimento == 'g':
    if litros_abastecimento <= 20:
        desconto5_por_litro = 1.90 * 0.04
        total_desconto = litros_abastecimento * desconto5_por_litro
        total_sem_desconto = litros_abastecimento * 1.90
        total_com_desconto = total_sem_desconto - total_desconto
        print(f'Você irá pagar: {total_com_desconto}\
              \nPreço sem desconto: {total_sem_desconto}\
              \nValor do desconto: {total_desconto}')

    if litros_abastecimento > 20:
        desconto5_por_litro = 2.50 * 0.06
        total_desconto = litros_abastecimento * desconto5_por_litro
        total_sem_desconto = litros_abastecimento * 2.50
        total_com_desconto = total_sem_desconto - total_desconto
        print(f'Você irá pagar: {total_com_desconto}\
              \nPreço sem desconto: {total_sem_desconto}\
              \nValor do desconto: {total_desconto}')


else:
    print('Escolha uma opção válida')
