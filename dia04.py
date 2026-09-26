# dia04.py - Loops e Listas (Estruturas de Repetição)

def calcular_orcamento(dias, custo_diario_usd, cotacao=5.50):
    total_usd = dias * custo_diario_usd
    total_brl = total_usd * cotacao
    return total_brl

# Lista de destinos para simular (Nome, Dias, Custo Diário em USD)
viagens = [
    {"destino": "Argentina", "dias": 7, "custo_usd": 40},
    {"destino": "Japão", "dias": 15, "custo_usd": 80},
    {"destino": "Tailândia", "dias": 30, "custo_usd": 35}
]

print("=== Simulação Automática de Múltiplas Viagens ===")

# O loop 'for' percorre cada item da lista automaticamente
for viagem in viagens:
    total_brl = calcular_orcamento(viagem["dias"], viagem["custo_usd"])
    print(f"Destino: {viagem['destino']} | {viagem['dias']} dias | Total: R$ {total_brl:.2f}")

print("-------------------------------------------------")