renda = float(input('Digite a renda mensal: R$ '))
idade = int(input('Digite a idade: '))
socre = float(input('Digite o score de crédito: '))
patrimonio = float(input('Digite o patrimônio: R$ '))
match (renda, idade, socre, patrimonio):
    case (renda, idade, socre, patrimonio) if renda >= 5000 and idade >= 25 and socre >= 800 and patrimonio >= 100000:
        print('Empréstimo aprovado')
    case (renda, idade, socre, patrimonio) if renda >= 3000 and idade >= 21 and socre >= 650 and patrimonio >= 50000:
        print('Empréstimo aprovado com restrições')
    case (renda, idade, socre, patrimonio) if renda >= 2000 and idade >= 18 and socre >= 600 and patrimonio >= 20000 or patrimonio == 0:
        print('Empréstimo reprovado, mas pode ser reconsiderado com garantias adicionais')
    case _:        print('Empréstimo reprovado')