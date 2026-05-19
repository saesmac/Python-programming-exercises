codigo = input('Digite o código de registro (AAAA-XX-9999): ')
ano = codigo[0:4]
curso = codigo[4:6]
numero = codigo[6:]
print(f'Ano: {ano}| Curso: {curso}| Número: {numero}')