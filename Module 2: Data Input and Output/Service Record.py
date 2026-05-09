def service_record(nome: str, idade: int, telefone: str, email: str, anotação: str) -> None:
    print(f"Nome: {nome} |Idade: {idade} |Telefone: {telefone} |Email: {email} |Anotação: {anotação}")
def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    anotação = input("Digite uma anotação: ")
    service_record(nome, idade, telefone, email, anotação)
if __name__ == "__main__":  main()