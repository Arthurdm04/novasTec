palavras = ['amor', 'roma', 'mora', 'carro', 'orça', 'orca', 'arco']

grupos = {}
for palavra in palavras:
    chave = tuple(sorted(palavra.lower()))  # ordena as letras da palavra para criar a chave
    
    if chave in grupos:
        grupos[chave].append(palavra)  # adiciona a palavra ao grupo existente
    else:
        grupos[chave] = [palavra]  # cria um novo grupo com a palavra

# Exibe os grupos formados
for chave, grupo in grupos.items():
    print(f'{chave}: {grupo}')
