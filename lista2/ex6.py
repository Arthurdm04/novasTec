# Crie um programa que some todos os números pares entre 1 e N, onde N é fornecido pelo usuário
num = int(input('Digite um número : '))
soma = 0
for num in range (1, num + 1):
    if num % 2 == 0:
        soma += num
print(f'A soma dos números pares entre 1 e {num} é: {soma}')
