qnt = int(input("Digite a quantidade de IDs: "))
for i in range(1, qnt + 1):
    if i % 2 == 0:
        continue  # ignora pares
    print(i, end=",")
print("\b ")  # remove a última vírgula