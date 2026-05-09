nome = input("Digite seu nome: ")
Quantos_anos = int(input('digite a quantos anos você fuma: '))
Macos_dia = int(input('digite quantos maços de cigarro você fuma por dia: '))
valor_maco = float(input('digite o valor de um maço de cigarro: '))
total_dias = Quantos_anos * 365
total_gasto = total_dias * Macos_dia * valor_maco
print(f"{nome}, você já gastou R${total_gasto:.2f} com cigarros ao longo de {Quantos_anos} anos.")
