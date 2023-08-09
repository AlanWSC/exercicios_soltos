# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))


if num1 > num2 and num2 > num3:
    print(f'O maior número é {num1}\nO menor número é {num3}')

elif num2 > num1 and num1 > num3:
    print(f'O maior número é {num2}\nO menor número é {num3}')

elif num3 > num1 and num1 > num2:
    print(f'O maior número é {num3}\nO menor número é {num2}')

elif num1 > num3 and num3 > num2:
    print(f'O maior número é {num1}\nO menor número é {num2}')

elif num2 > num3 and num3 > num1:
    print(f'O maior número é {num2}\nO menor número é {num1}')

elif num3 > num2 and num2 > num1:
    print(f'O maior número é {num3}\nO menor número é {num1}')

elif num1 == num2 and num2 < num3:
    print(f'O maior número é {num3}\nO menor número é {num1}')

elif num1 == num3 and num3 < num2:
    print(f'O maior número é {num2}\nO menor número é {num1}')

elif num1 == num3 and num3 < num2:
    print(f'O maior número é {num2}\nO menor número é {num1}')

elif num1 == num3 and num3 < num2:
    print(f'O maior número é {num2}\nO menor número é {num1}')


# if num1 > num2 and num1 > num3:
#    print(f'O maior número é {num1}')

# elif num2 > num1 and num2 > num3:
#    print(f'O maior número é {num2}')

# elif num3 > num1 and num3 > num2:
#    print(f'O maior número é {num3}')
# else:
#    print('Os números são iguais')
