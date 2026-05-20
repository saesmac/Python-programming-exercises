fila = []
nome = input("Digite o nome do paciente (ou 'sair' para encerrar): ")
while nome.lower() != 'sair':
    fila.append(nome)
    print(f"Paciente '{nome}' adicionado à fila.")
    nome = input("Digite o nome do paciente (ou 'sair' para encerrar): ")  
print("\n=== Fila de Atendimento ===")
while fila:
    paciente_atendido = fila.pop(0)  # Remove o primeiro paciente da fila
    print(f"Atendendo paciente: {paciente_atendido}")
print("Todos os pacientes foram atendidos.")