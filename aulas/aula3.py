contador = 0

# Enquanto o contador for menor que 5, o loop continuará
while contador < 5:
    print(f'Contador: {contador}')
    contador += 1  # Incrementa o contador a cada iteração


# For
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

# Range 
for i in range(3, 8):
    print(i)

"""
Explicação do range():
range(stop): Cria uma sequência de números que começa de 0 até stop - 1. O número de término (stop) não é incluído na sequência.

range(start, stop): Cria uma sequência de números começando em start até stop - 1. O número de término (stop) também não é incluído na sequência.

range(start, stop, step): Cria uma sequência de números começando em start, terminando antes de stop, com um incremento (ou decremento) de step. O valor de step define o intervalo entre os números gerados. O valor de step pode ser:

Positivo: Para gerar uma sequência crescente (de start até stop).
Negativo: Para gerar uma sequência decrescente (de start até stop).
Exemplo de range():

range(5) gera os números de 0 a 4.
range(3, 8) gera os números de 3 a 7.
range(0, 10, 2) gera os números de 0 a 8, com incremento de 2.
range(10, 0, -2) gera os números de 10 a 2, com decremento de 2.
"""



# Lista de bandas
bandas = ['Metalica', 'Slipknot', 'Fabio e Fabiano']

# Enumerando e imprimindo as bandas com seus índices
for indice, banda in enumerate(bandas): # indice = Recebe o índice de cada item (0, 1, 2, etc.).    
    print(f"{indice + 1}. {banda}")  # Começar a contagem pelo 1
