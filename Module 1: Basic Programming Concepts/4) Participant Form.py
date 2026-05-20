nome = input("Digite o nome do participante: ")
idade = int(input("Digite a idade do participante: "))
cidade = input("Digite a cidade do participante: ")
curso = input("Digite o curso do participante: ")
if curso.lower() != "programação":
    print(f"{nome} não está inscrito no curso de programação e não pode participar.")
elif idade < 18:
    print(f"{nome} é menor de idade e não pode participar.")
else:
    print(f'{nome} , com {idade} anos, de {cidade}, está apto a participar.')