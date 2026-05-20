#Entrada lista de notas
notas = [float(x) for x in input("Digite as notas dos alunos (separadas por espaço): ").split()]

#Cálculos principais
media = sum(notas) / len(notas) 
maior_nota = max(notas)
menor_nota = min(notas)
aprovados = sum(1 for nota in notas if nota >= 7.0)

#Exibição dos resultados
print("\n=== Boletim Escolar ===")
print(f" Média da turma: {media:.2f}")
print(f" Maior nota: {maior_nota}")
print(f" Menor nota: {menor_nota}")
print(f" Alunos aprovados: {aprovados}")