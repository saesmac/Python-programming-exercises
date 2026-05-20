
produtos = []  
print("Digite os produtos da lista (ou 'finalizar' para encerrar):")    
while True:
    item = input(f"Digite o nome do item {len(produtos)+1}: ")
    if item.lower() == 'finalizar':
        break
    produtos.append(item.strip().lower())  # Armazena o item em minúsculo e sem espaços extras

#remova itns indisponiveis
while True:
    indisponivel = input("Quer remover algum item? se nao digite 'n': ").strip().lower()
    if indisponivel == '':
        item_remover = input("Digite o nome do item a ser removido: ").strip().lower()
        if item_remover in produtos:
            produtos.remove(item_remover)
            print(f"Item '{item_remover}' removido da lista.")
    elif indisponivel == 'n':
        break
    else:
        print(f"Item '{indisponivel}' não encontrado na lista.")


#ordena alfabeticamente
produtos.sort()
print("\n=== Lista de Compras ===")
for item in produtos:
    print(f"- {item.capitalize()}")  # Exibe o item com a primeira letra maiúscula