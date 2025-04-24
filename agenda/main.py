import datetime
from agenda import Contato

nome = input('Digite seu nome: ')
numero = input('Digite seu número: ')
strdata = input('Digite sua data de nascimento (dd/mm/aaaa): ')
datanasc = datetime.datetime.strptime(strdata, "%d/%m/%Y")  # Corrigido aqui
email = input('Digite seu email: ')

contato1 = Contato(nome, numero, datanasc, email)  # Corrigido aqui

print(f'Seu primeiro contato é:\nNome: {contato1.nome}\nNúmero: {contato1.numero}\nData de Nascimento: {contato1.datanasc}\nEmail: {contato1.email}')
