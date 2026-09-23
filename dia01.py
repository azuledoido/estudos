# --- EXERCÍCIO DIA 01: LÓGICA E ENTRADA DE DADOS ---

print("=== BEM-VINDO AO PLANEJADOR NÔMADE ===")

# 1. Entrada de dados (todas as perguntas juntas no inicio)
nome = input("Digite seu nome de usuario: ")
destino = input("Qual destino voce quer conhecer (ex: Tailandia)? ")
dias = int(input("Quantos dias pretende ficar la (digite apenas o numero)? "))
custo_diario_usd = float(input("Custo diario estimado em Dolares (USD): "))
passagem_brl = float(input("Custo estimado da passagem aerea em Reais (R$): "))

# 2. Processamento (todos os calculos)
custo_total_usd = dias * custo_diario_usd
cotacao_dolar = 5.50
custo_total_brl = (custo_total_usd * cotacao_dolar) + passagem_brl

# 3. Saida de dados (exibição do resultado final)
print("\n----------------------------------")
print(f"Ola, {nome}!")
print(f"Sua viagem para {destino} de {dias} dias custara:")
print(f"-> US$ {custo_total_usd:.2f} Dolares (hospedagem/gastos)")
print(f"-> R$ {passagem_brl:.2f} Reais (passagem aerea)")
print(f"-> R$ {custo_total_brl:.2f} Reais (CUSTO TOTAL DA VIAGEM)")
print("----------------------------------")