def aplicar_desconto(preco: float, desconto_percentual: float) -> float:
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))
novo_preco = aplicar_desconto(preco, desconto)
print(f"Preço com desconto: R$ {novo_preco:.2f}")
