# Senha definida pelo sistema
senha_correta = "1234"

#Número máximo de tentativas
max_tentativas = 3

for tentativa in range(1, max_tentativas + 1):
    # Solicitar ao usuário que insira a senha
    senha_usuario = input("Digite a senha para acessar sua conta: ")
    
    # Verificar se a senha está correta
    if senha_usuario == senha_correta:
        print("Acesso concedido. Bem-vindo ao seu caixa eletrônico!")
        break  # Sair do loop se a senha estiver correta
    else:
        print(f"Senha incorreta. Tentativa {tentativa} de {max_tentativas}.")
        
        # Verificar se o número máximo de tentativas foi atingido
        if tentativa == max_tentativas:
            print("Número máximo de tentativas atingido. A conta foi bloqueada.")
