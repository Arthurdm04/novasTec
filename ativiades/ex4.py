# Crie um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) aparecem na frase. Considere que a contagem deve ser case-insensitive (ou seja, não diferencie maiúsculas de minúsculas)
frase = input('Digite uma frase: ')

frase = frase.lower()
vogais = 0

for caractere in frase:
    if caractere in 'aeiou':
        vogais += 1

print('O número de vogais na frase é {}'.format(vogais))
