#  Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos individuais e imprime os dígitos separados uns dos outros por três espaços cada. Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9

num = int(input('Digite cinco números: '))
if 10000 <= num <= 99999:
    dig1 = num // 10000
    dig2 = (num // 1000) % 10
    dig3 = (num // 100) % 10
    dig4 = (num // 10) % 10
    dig5 = num % 10

    print(dig1,dig2,dig3,dig4,dig5)
else:
    print('Número inválido!')
