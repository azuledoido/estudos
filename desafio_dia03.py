# desafio_dia03.py

def calcular_orcamento(dias, custo_diario_usd, cotacao=5.50):
    total_usd = dias * custo_diario_usd
    total_brl = total_usd * cotacao
    return total_usd, total_brl

def classificar_viagem(custo_brl):
    if custo_brl < 3000:
        return "Económica"
    elif custo_brl <= 7000:
        return "Moderada"
    else:
        return "Alto Custo / Luxo"

def calcular_reserva_emergencia(custo_brl, dias):
    if dias > 30:
        return custo_brl * 0.20
    else:
        return custo_brl * 0.10

# --- Execução Principal ---
print("=== Calculadora com Reserva de Emergência ===")

nome = input("Digite o seu nome: ")
destino = input("Destino pretendido: ")
dias = int(input("Quantidade de dias: "))
custo_diario = float(input("Custo diário estimado (USD): "))

usd_total, brl_total = calcular_orcamento(dias, custo_diario)
categoria = classificar_viagem(brl_total)
reserva = calcular_reserva_emergencia(brl_total, dias)
total_geral = brl_total + reserva

print("\n----------------------------------")
print(f"Olá, {nome}!")
print(f"Viagem para {destino} ({dias} dias)")
print(f"Custo Base em Reais: R$ {brl_total:.2f}")
print(f"Reserva de Emergência Recomendeda: R$ {reserva:.2f}")
print(f"Custo Total Geral (Viagem + Reserva): R$ {total_geral:.2f}")
print(f"Categoria do Orçamento: {categoria}")
print("----------------------------------")