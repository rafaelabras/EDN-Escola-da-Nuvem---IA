try:
 senha = input("Insira sua senha:")
 tamanho = senha.__len__()

 if (len(senha) < 8):
    raise ValueError("A senha deve possuir 8 caracteres.")
 
 if not any(char.isdigit() for char in senha):
     raise ValueError("A senha deve conter pelo menos um número.")

 raise ValueError("Sua senha deve ter um numero ")


except ValueError as e:
  print("Erro, ",e)