# Uma empresa que quer enviar dados pela internet pediu-lhe que escrevesse um programa que criptografe dados a fim de que eles possam ser transmitidos com maior segurança. Todos os dados são transmitidos como inteiros de quatro dígitos. Seu aplicativo deve ler um inteiro de quatro dígitos inserido pelo usuário e criptografá-lo da seguinte maneira: substitua cada dígito pelo resultado da adição de 7 ao dígito, obtendo o restante depois da divisão do novo valor por 10. Troque então o primeiro dígito pelo terceiro e o segundo dígito pelo quarto. Então, imprima o inteiro criptografado. Escreva um aplicativo separado que receba a entrada de um inteiro de quatro dígitos criptografado e o descriptografe (revertendo o esquema de criptografia) para formar o número original.
def criptografar(numero):
    """Criptografa um número inteiro de quatro dígitos."""

    # Verificar se o número tem quatro dígitos
    if not (1000 <= numero <= 9999):
        return "Número inválido. Deve ter quatro dígitos."

    # Converter o número para uma lista de dígitos
    digitos = [int(d) for d in str(numero)]

    # Substituir cada dígito
    digitos = [(d + 7) % 10 for d in digitos]

    # Trocar o primeiro dígito pelo terceiro e o segundo pelo quarto
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    # Converter a lista de dígitos de volta para um inteiro
    numero_criptografado = int("".join(map(str, digitos)))

    return numero_criptografado

# Exemplo de uso
numero_original = int(input("Digite um número de quatro dígitos para criptografar: "))
numero_criptografado = criptografar(numero_original)
print("Número criptografado:", numero_criptografado)
