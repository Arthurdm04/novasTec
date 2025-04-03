# Funções
def soma1(a,b):
    '''
    Função para calcular soma entre dois números 
    '''
    return a+b
print(soma1.__doc__) # Printa o comentário
print(soma1(10,5))


def calculadora(a,b):
    return a+b, a-b, a*b, a//b
soma, sub, mult, div = calculadora(10,2)
print(soma)
print(sub)
print(mult)
print(div)


def calculadoraa(**kwargs):
    for chave, valores in  kwargs.items():
        match chave:
            case '+':
                for valor in valores:
                    soma+=valor
            case '-':
                sub=0
                for valor in valores:
                    sub-=valores
            case '*':
                mult=1
                for valor in valores:
                    mult*=valor
            case '/':
                div=1
                for valor in valores:
                    div/=valores
    return soma, sub, mult, div
                


dic = {'+': [1,2,3], '-': [10,2,3], '*': [3,4,9], '/': [10,2,3]}

soma, sub, mult, div = calculadoraa(**dic)

print(soma)
print(sub)
print(mult)
print(div)