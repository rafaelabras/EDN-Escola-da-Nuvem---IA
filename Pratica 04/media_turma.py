aluno = int(input("Quantos alunos tem na sala?: "))
notas = []
total = 0

for i in range(aluno):
 valor = float(input(f"Insira a nota do aluno {i + 1}: "))
 notas.append(valor)
 total = total + valor

media = total/aluno
print("A media total é: ", media)  