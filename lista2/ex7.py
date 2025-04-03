#  Escreva um aplicativo que solicita ao usuário que insira o tamanho do lado de um quadrado e, então, exibe um quadrado vazio desse tamanho com asteriscos. Seu programa deve trabalhar com quadrados de todos os comprimentos de lado possíveis entre 1 e 20.
tamanho = int(input("Digite o tamanho do lado do quadrado (1-20): "))

# Valida se o tamanho está entre 1 e 20
if tamanho < 1 or tamanho > 20:
    print("Tamanho inválido! Digite um valor entre 1 e 20.")
else:
    # Loop para cada linha do quadrado
    for linha in range(tamanho):
        # Se for a primeira ou última linha, imprime uma linha cheia de asteriscos
        if linha == 0 or linha == tamanho - 1:
            print('* ' * tamanho)
        else:
            # Caso contrário, imprime asteriscos apenas nas bordas
            print('* ' + '  ' * (tamanho - 2) + '*')
            