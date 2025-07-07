try:
 numeros = []
 i = 1
 par, impar = 0

 while i == 1:
       numero = int(input("Insira um numero: "))
       numeros.append(numero)

       if (numero % 2 == 0):
         par = par + 1

       if (numero % 2 != 0):
          impar = impar + 1
    
       i = int(input("Deseja inserir mais um numero? 0-nao 1-sim"))
 print("Valor de numeros pares: ", par)
 print("Valor de numeros impares: ", impar)
 
except ValueError as e:
 print("Erro", e)
