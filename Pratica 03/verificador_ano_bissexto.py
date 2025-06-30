try:
 ano = int(input("Insira o ano para verificar se ele é bissexto: "))
 if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
   print("O ano eh bissexto")
 else:
   print("O ano não eh bissexto.")

except ValueError as e:
    print("Erro:", e)
