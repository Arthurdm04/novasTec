class Contato:
    __slots__ = ['_nome', '_numero', '_datanasc', '_email']

    def __init__(self, nome, numero, datanasc, email):
        self._nome = nome
        self._numero = numero
        self._datanasc = datanasc
        self._email = email

    # Properties (getters/setters) permanecem iguais
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
    
    @property
    def datanasc(self):
        return self._datanasc
    
    @datanasc.setter
    def datanasc(self, datanasc):
        self._datanasc = datanasc
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f"Nome: {self.nome} | Número: {self.numero} | Nascimento: {self.datanasc.strftime('%d/%m/%Y')} | Email: {self.email}"