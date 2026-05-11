idade = int(input('Digite a idade: '))
if idade >= 18:
    print('Entrada permitida.')
else:
    autorização = input('Entrada proibida. Você tem autorização dos seus pais? (s/n) ')
    if autorização.lower() == 's':
        print('Entrada permitida com autorização dos pais.')
    else:        print('Entrada proibida sem autorização dos pais.')
    