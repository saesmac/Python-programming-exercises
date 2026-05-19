Nota_final = float(input('Digite a nota final do aluno: '))
Frequencia = float(input('Digite a frequência do aluno (em %): '))
match (Nota_final, Frequencia):
    case (nota, freq) if nota >= 7.0 and freq >= 75.0:
        print('Aprovado')
    case (nota, freq) if nota > 5.0 and nota < 6.9 and freq >= 75.0:
        print('Recuperação')
    case (nota, freq) if nota < 5.0 and freq >= 75.0:
        print('Reprovado por nota')
    case _:
        print('Reprovado')