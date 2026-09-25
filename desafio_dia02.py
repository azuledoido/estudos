# desafio_dia02.py

# 1. Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))

# 2. Processamento (Cálculo da média)
media = (nota1 + nota2) / 2

# 3. Saída de dados (Frase formatada)
print(f"O aluno {nome} ficou com média {media:.1f}")
