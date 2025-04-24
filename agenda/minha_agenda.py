from Contato import Contato  # Alterado aqui

class Agenda:
    def __init__(self):
        self._contatos = []

    def adicionar_contato(self, contato):
        self._contatos.append(contato)

    def buscar_contato(self, nome):
        for c in self._contatos:
            if c.nome.lower() == nome.lower():
                return c
        return None

    def remover_contato(self, nome):
        c = self.buscar_contato(nome)
        if c:
            self._contatos.remove(c)
            return True
        return False

    def listar_contatos(self):
        print("\n--- Lista de Contatos ---")
        for c in self._contatos:
            print(c)  # Chama __str__ automaticamente