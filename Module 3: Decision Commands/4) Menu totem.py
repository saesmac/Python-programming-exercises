opçao = int(input('Digite uma opção (1-4): '))
match opçao:
    case 1:
        print('Fazer pedido ')
    case 2:        print('Adicionar item')
    case 3:        print('Consultar pedido')
    case 4:        print('Cancelar pedido')
    case _:        print('Opção inválida')
