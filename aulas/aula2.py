turno = input('Turno de aula: \n' + 'M - Matutino\n' + 'V - Vespertino\n' + 'N - noturno:\n')

match turno:
    case 'm':
        print('Estuda no Matutino')
    case 'v':
        print('Estuda no Vespertino')
    case 'n':
        print('Estuda no Noturno')
    case _:
        print('Inexistente')
    