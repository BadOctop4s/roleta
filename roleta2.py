import random
import time
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def roleta_decisoes(opcoes):
    limpar_terminal()
    print("🎯 Iniciando a roleta de decisões...\n")

    for i in range(15):
        escolha = random.choice(opcoes)
        print(f"🎲 {escolha}")
        time.sleep(0.1 + i * 0.03)
        limpar_terminal()

    decisao = random.choice(opcoes)
    print("🔔 A roleta escolheu:")
    print(f"\n👉 {decisao} 👈\n")

def pegar_opcoes_uma_linha():
    entrada = input("Digite as opcoes separadas por virgulas: ").strip()
    opcoes = [opcao.strip() for opcao in entrada.split(',') if opcao.strip()]
    return opcoes

opcoes = pegar_opcoes_uma_linha()

if len(opcoes) < 2:
    print("\n🤚 Voce precisa de pelo menos 2 opcoes para usar a roleta.")
else:
    roleta_decisoes(opcoes)
