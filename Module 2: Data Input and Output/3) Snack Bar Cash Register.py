def calculate_total(items):
    total = 0
    resumo = []
    for i, item in enumerate(items, start=1):
        subtotal = item['valor'] * item['quantidade']
        total += subtotal
        resumo.append(f"Item {i}: {item['name']} - R$ {subtotal:.2f}")
    return resumo, total

def main():
    items = []
    while True:
        name = input("Digite o nome do item (ou 'finalizar' para terminar): ")
        if name.lower() == 'finalizar':
            break
        price = float(input("Digite o preço do item: "))
        quantidade = int(input("Digite a quantidade do item: "))
        items.append({'name': name, 'valor': price, 'quantidade': quantidade})
    
    resumo, total = calculate_total(items)
    recibo = " | ".join(resumo)
    print(f"{recibo} | Total: R$ {total:.2f}")

if __name__ == "__main__":
    main()
