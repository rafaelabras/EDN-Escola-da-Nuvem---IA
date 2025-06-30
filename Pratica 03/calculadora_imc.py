
try:
 imc = float(input("Insira seu IMC "))
 if(imc < 0):
      raise ValueError("Não é permitido seu IMC ser negativo.")
 if (imc < 18.5):
      print("Abaixo do peso")
 if (imc < 25 and imc >= 18.5):
      print("Peso normal")
 if (imc <= 30 and imc >= 25):
      print("Sobrepeso")
 if (imc > 30):
      print("Obeso")
except ValueError as e:
    print("Erro:", e)
