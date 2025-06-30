valor_em_reais = float(input("Digite o valor em reais (R$): "))
taxaDolar = 5.49
taxaEuro = 6.31

valorEmDolar = valor_em_reais / taxaDolar

valorEmEuro = valor_em_reais / taxaEuro

print(f"R$ {valor_em_reais:.2f} equivale a:")
print(f"$ {valorEmDolar:.2f} dolares")
print(f"$ {valorEmEuro:.2f} euro:")