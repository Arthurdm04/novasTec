def descriptografar(numero_criptografado):
    """Descriptografa um número inteiro de quatro dígitos criptografado."""

    # Verificar se o número tem quatro dígitos
    if not (1000 <= numero_criptografado <= 9999):
        return "Número inválido. Deve ter quatro dígitos."

    # Converter o número criptografado para uma lista de dígitos
    digitos = [int(d) for d in str(numero_criptografado)]

    # Reverter a troca de dígitos
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    # Reverter a substituição de dígitos
    digitos = [(d - 7) % 10 for d in digitos]

    # Converter a lista de dígitos de volta para um inteiro
    numero_original = int("".join(map(str, digitos)))

    return numero_original

# Exemplo de uso
numero_criptografado = int(input("Digite um número de quatro dígitos criptografado para descriptografar: "))
numero_original = descriptografar(numero_criptografado)
print("Número original:", numero_original)