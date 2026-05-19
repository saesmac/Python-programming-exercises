# se quer uma tabuada especifica?
numero = int(input("Digite um número para ver sua tabuada ou 1 para completa: "))
if numero >= 2:
    print(f"Tabuada do {numero}:")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
else:
#Tabuada de 2 ao 10
    for numero in range(2, 11):
        print(f"Tabuada do {numero}:")
        for multiplicador in range(1, 11):
            resultado = numero * multiplicador
            print(f"{numero} x {multiplicador} = {resultado}")
        print()  # Linha em branco para separar as tabuadas