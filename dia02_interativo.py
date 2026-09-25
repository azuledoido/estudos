# O input() faz o programa esperar o utilizador digitar algo
nome = input("Qual é o seu nome? ")
produto = input("Qual produto deseja comprar? ")

# Exibindo os dados capturados
print(f"Olá, {nome}! Você escolheu o produto: {produto}")
# Convertendo o texto digitado para float e int
preco = float(input("Digite o preço do produto (ex: 250.00): "))
quantidade = int(input("Digite a quantidade: "))

# Agora podemos calcular normalmente
total = preco * quantidade

print(f"Total a pagar pelo estoque de {produto}: R$ {total}")