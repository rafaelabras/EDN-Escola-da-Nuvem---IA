
try:
 escolha1 = int(input("Escolha a temperatura para inserir (1-celsius,2-kelvin,3-fahrenheit): "))
 temp = float(input("Insira a temperatura: "))
 escolha2 = int(input("Agora escolha para qual temperatura vc quer converter: (1-celsius,2-kelvin,3-fahrenheit)"))
 
 if (escolha1 == escolha2):
    raise ValueError("Insira uma escolha valida, as duas opções foram iguais.")
 
 if (escolha1 == 1 and escolha2 == 2):
    temp = temp + 273.15

 if (escolha1 == 1 and escolha == 3):
    temp = (temp * 1.8) + 32

 if(escolha1 == 2 and escolha2 == 1):
    temp = temp - 273.15

 if(escolha1 == 2 and escolha2 == 3):
    temp = (temp * 1.8) - 459.67

 if(escolha1 == 3 and escolha2 == 1):
    temp = (temp - 32)/1.8

 if(escolha1 == 3 and escolha2 == 2):
    temp = (temp + 459.67)/1.8

except ValueError as e:
    print("Erro:", e)
