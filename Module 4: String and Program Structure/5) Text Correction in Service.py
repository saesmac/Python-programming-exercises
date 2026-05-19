frase = input("Digite uma frase com abreviação: ")

frase_corrigida = frase.replace("vc", "você").replace("tb", "também").replace("q", "que").replace("pq", "porque").replace("blz", "beleza").replace("flw", "falou").replace("vlw", "valeu")

print(frase_corrigida)