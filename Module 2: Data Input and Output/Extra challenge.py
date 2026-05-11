def ficha():
    nome = input('Digite o nome do cliente: ')
    idade = input('Digite a idade do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    Valor = float(input('Digite o valor da compra:'))
    Cotação = float(input("Digite a cotação do dólar: "))
    Dolar = Valor / Cotação
    print(f"Ficha do cliente: Nome: {nome} | Idade: {idade} | Telefone: {telefone}")
    print(f"O valor em Dólar é: {Dolar:.2f}")
ficha() 
