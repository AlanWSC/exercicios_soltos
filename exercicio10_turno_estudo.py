# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

mensagem = input(
    'Digite o turno que você estuda: \nM - Matutino\nV - Vespertino\nN - Noturno\n')

if mensagem == 'M' or mensagem == 'm' or mensagem == 'Matutino' or mensagem == 'matutino':
    print('Seu turno é Matutino. Bom dia!!')

elif mensagem == 'V' or mensagem == 'v' or mensagem == 'Vespertino' or mensagem == 'vespertino':
    print('Seu turno é Vespertino. Boa tarde!!')

elif mensagem == 'N' or mensagem == 'n' or mensagem == 'Noturno' or mensagem == 'noturno':
    print('Seu turno é Noturno. Boa noite!!')

else:
    print('Turno inválido')
