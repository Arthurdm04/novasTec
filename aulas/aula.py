'''
if 5 > 6:
    print('Verdade')
else:
    print('Falso')
'''

# Cálculo de média
n1 = float(input('Digita a nota 1: '))
n2 = float(input('Digita a nota 2: '))
n3 = float(input('Digita a nota 3: '))

media = (n1+n2+n3)/3

if media < 3:
    print('Reprovado')
elif media >= 3 and media < 7:
    print('Recuperação')
else:
    print('Aprovado')
    