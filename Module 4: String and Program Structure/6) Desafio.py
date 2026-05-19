nome = input('Digite o nome do cliente: ').strip()
sobrenome = input('Digite o sobrenome do cliente: ').strip()
codigo = input("Digite o código de matrícula (AAAA-XX-9999): ").strip()

email = f"{nome.lower()}.{sobrenome.lower()}@escola.com"

ano = codigo[0:4]
curso = codigo[4:6]
numero = codigo[6:]

print('Ficha de Matrícula')
print('Nome'.ljust(12, ".") + f'{nome} {sobrenome}'.rjust(15))
print('Email'.ljust(12, ".") + email.rjust(15))
print('Ano'.ljust(12, ".") + ano.rjust(15))
print('Curso'.ljust(12, ".") + curso.rjust(15))
print('Número'.ljust(12, ".") + numero.rjust(15))
print('------------------------')