import datetime
from Contato import Contato  # Alterado aqui

try:
    nome = input('Digite seu nome: ')
    numero = input('Digite seu número: ')
    strdata = input('Digite sua data de nascimento (dd/mm/aaaa): ')
    datanasc = datetime.datetime.strptime(strdata, "%d/%m/%Y")
    email = input('Digite seu email: ')

    contato1 = Contato(nome, numero, datanasc, email)
    print(f"\nContato criado:\n{contato1}")  # Usa o __str__

except ValueError:
    print("\nErro: Formato de data inválido! Use dd/mm/aaaa.")