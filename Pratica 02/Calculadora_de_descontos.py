produto = input("Insira o nome do produto: ")
preco_original = float(input("Insira o preco original: "))
porcentagem = int(input("Insira a porcentagem de desconto: "))
desconto = preco_original - (preco_original * (porcentagem/100))

print("Produto: ", produto)
print("Preco original: ", preco_original)
print("Preco com desconto: ", desconto)

