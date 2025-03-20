# Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando asteriscos (*).
def desenhar_caixa():
  """Desenha uma caixa usando asteriscos."""
  print("***")
  print("* *")
  print("* *")
  print("***")


def desenhar_oval():
  """Desenha um oval usando asteriscos."""
  print("    **** ")
  print("  *       *")
  print(" *         *")
  print('*           *')
  print(" *         *")
  print("    *** ")



def desenhar_seta():
  """Desenha uma seta usando asteriscos."""
  print("  * ")
  print(" *** ")
  print("*****")
  print("  * ")
  print("  * ")


def desenhar_losango():
  """Desenha um losango usando asteriscos."""
  print("  * ")
  print(" *** ")
  print("*****")
  print(" *** ")
  print("  * ")


def main():
  """Função principal para exibir as formas."""
  print("Caixa:")
  desenhar_caixa()

  print("\nOval:")
  desenhar_oval()

  print("\nSeta:")
  desenhar_seta()

  print("\nLosango:")
  desenhar_losango()

if __name__ == "__main__":
  main()
  