# Explicando listas
lista1 = ['UCB', 'UNB', 'UDF', 'UNIEURO']
lista2 = [1, 'UCB', 1.6, 'Unb']
lista3 = ['UnDF', 'UCB', 6, 9.87, 3.1415789, range(20)]
lista5 = ['catolica']
lista6 = list(range(20))
lista7 = [lista1, lista2, lista3, lista5, lista6]

print(lista1)
print(lista2)
print(lista3)
print(lista5)
print(lista6)
print(lista7)

print(lista1[1])
print(lista1[-1])
print(lista1[::1])


# Exemplo de lista com for, calculando uma média
notas = [6, 8, 9]
soma = 0
for nota in notas:
    soma = soma + nota
#print(f'Média é {soma/3:.2f}')
print(f'Média é {soma/len(notas):.2f}')


# L = V
L = [2,3,4,5]
V = L
print(V)
V[1] = 10
print(L)
L[2] = -9
print(V)

# Métodos para adicionar objetos na lista ou remover, tem mais métodos com outras funções
lista=[]
lista.append(10)
print(lista)
lista.append(-3)
print(lista)
lista.pop() # Pop tira o último que entrou na lista
print(lista)
lista.extend([3, 6, 8, 9]) # Extend posso adicionar mais de um item na lista, não esqeucer dos colcetes []
print(lista)


# Dar uma olhada depois no map
list(map(lambda x: x**2, [2, 6, 7]))


#Listas com elementos de tipos diferentes
produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2,produto3]
print(compras)
for e in compras:
	print(f"Produto: {e[0]} ")
	print(f"Quantidade: {e[1]}")
	print(f"Preço: {e[2]:5.2f}")


# Tuplas
#tupla = (1,2,3,4,5)
#tupla[0] = 10 # Nesse exemplo, uma lista normal mudaria o elemento 0 para 10, com a tupla ela não mudará e dará erro

# Nesse exemplo mostra que a tupla pode ser alterada dentro da lista, se não fosse a lista ela não poderia ser mudada
tupla1 = (1,2,3)
tupla2 = (4,5,6)
listA = [tupla1, tupla2]
print(listA)
listA[0] = (7,8,9)
print(listA)

# Tuplas
*a,b = [10,20,30]
print(*a,b) # Resulta em a = 10,20 e b = 30
#a,*b = [10,20,30]
#print(a,*b) # Resulta em a = 10 e b = 20,30


# Conjuntos
fruta = set(['banana', 'abacaxi', 'pera'])
print(fruta)


# Dicionário
salas = {'10': 15, '15': 200, '3': 4}
print(salas['15'])

pessoa = {'Nome' : 'Arthur', 'idade': 21, 'cidade': 'Luziania', 'sexo': 'M'}
print(pessoa['Nome'])
print(pessoa['idade'])
print(pessoa['cidade'])
print(pessoa['sexo'])
