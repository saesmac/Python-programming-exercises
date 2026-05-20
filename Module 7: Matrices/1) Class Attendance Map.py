#Mapa de presença em sala de aula
# 1=Presente 0=Ausente
#Matriz 4x4
presencas = []

print('Digite a presença dos alunos (1 para presente, 0 para ausente):')
for i in range(4):
    linha = input(f'Linha {i+1}:')
    valores = [int(x) for x in linha.split()]
    presencas.append(valores)

#Somar as presenças de cada aluno
total_presentes = sum(sum(linha) for linha in presencas)

#Exibir o total de presenças
print('\n=== Resultado ===')
print("Mapa de Presença:", presencas)
print("Quantidade total de alunos presentes:", total_presentes)