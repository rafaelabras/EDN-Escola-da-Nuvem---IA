try:
    
 operacao = int(input("Selecione a operacao: 1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão\n"))

 while(operacao not in [1, 2, 3, 4]):
    operacao = int(input("Selecione a operacao: 1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão\n"))

 try:
     numero1 = float(input("Insira o primeiro numero da calculadora: \n"))
     numero2 = float(input("Insira o segundo numero da calculadora: \n"))
 except ValueError as e:
     print("Digite um numero.", e)
     exit()

 if operacao == 4 and numero2 == 0:
     raise ValueError("Divisao por zero não é permitida.")
 
 elif operacao == 1:
     resultado = numero1 + numero2

 elif operacao == 2:
     resultado = numero1 - numero2

 elif operacao == 3:
     resultado = numero1 * numero2

 elif operacao == 4:
     resultado = numero1 / numero2

 print("Resultado = ", resultado)

except ValueError as e:
     print("Erro:", e)