produto = input("Insira o nome do produto: ")
preco = float(input("Insira o preço do produto: "))
quantidade = int(input("Insira a quantidade do produto: "))

print("Nome do produto: ", produto)
print("Preco do produto: ", preco)
print("Preço total de acordo com a quantidade e o produto: ", quantidade * preco)