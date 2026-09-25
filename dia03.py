# dia03.py - Tomada de Decisão e Funções

def calcular_orcamento(dias, custo_diario_usd, cotacao=5.50):
    """Calcula o custo total em dólares e reais."""
    total_usd = dias * custo_diario_usd
    total_brl = total_usd * cotacao
    return total_usd, total_brl

def classificar_viagem(custo_brl):
    """Classifica a viagem com base no custo total em Reais."""
    if custo_brl < 3000:
        return "Económica"
    elif custo_brl <= 7000:
        return "Moderada"
    else:
        return "Alto Custo / Luxo"

# --- Execução Principal ---
print("=== Calculadora de Viagem v3.0 ===")

nome = input("Digite o seu nome: ")
destino = input("Destino pretendido: ")
dias = int(input("Quantidade de dias: "))
custo_diario = float(input("Custo diário estimado (USD): "))

# Uso das funções
usd_total, brl_total = calcular_orcamento(dias, custo_diario)
categoria = classificar_viagem(brl_total)

print("\n----------------------------------")
print(f"Olá, {nome}!")
print(f"Viagem para {destino} ({dias} dias)")
print(f"Custo em Dólares: US$ {usd_total:.2f}")
print(f"Custo em Reais: R$ {brl_total:.2f}")
print(f"Categoria do Orçamento: {categoria}")
print("----------------------------------")