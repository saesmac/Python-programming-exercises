# Faixa fixa de 1 a 50
for i in range(1, 51):
    if i % 5 == 0:
        # Destacar múltiplos de 5 com marca visual
        print(f"[{i}*]", end=",")
    else:
        print(i, end=",")