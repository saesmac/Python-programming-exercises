def soma_media_notas(n1: float, n2: float, n3: float) -> None:
    soma = n1 + n2 + n3
    media = soma / 3
    print(f"A soma das notas é: {soma:.2f} | A média das notas é: {media:.2f}")
def main():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    soma_media_notas(n1, n2, n3)
if __name__ == "__main__":  main()