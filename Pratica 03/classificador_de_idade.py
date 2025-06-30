
try:
 idade = int(input("Insira sua idade: "))
 if(idade <0):
      raise ValueError("Não é permitido sua idade ser negativa.")
 if (idade > 0 and idade <= 12):
      print("Criança")
 if (idade >= 13 and idade <= 17):
      print("Adolescente")
 if (idade >= 18 and idade <= 59):
      print("Adulto")
 if (idade >= 60):
      print("Idoso")
except ValueError as e:
    print("Erro:", e)
