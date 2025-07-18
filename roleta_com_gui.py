import tkinter as tk
import random
import time
from threading import Thread

def escolher_opcao():
    texto = entrada_opcoes.get()
    opcoes = [opcao.strip() for opcao in texto.split(',') if opcao.strip()]

    if len(opcoes) < 2:
        resultado_var.set("⚠️ Digite pelo menos 2 opções separadas por vírgula.")
        return

    def animar():
        resultado_var.set("🎯 Girando...")
        for i in range(15):
            escolha = random.choice(opcoes)
            resultado_var.set(f"🎲 {escolha}")
            time.sleep(0.1 + i * 0.03)
        decisao = random.choice(opcoes)
        resultado_var.set(f"👉 {decisao} 👈")

    Thread(target=animar).start()  # evita travar a janela

# Janela principal
janela = tk.Tk()
janela.title("Roleta de Decisões 🎲")
janela.geometry("400x250")
janela.resizable(False, False)

# Campo de entrada
label_instrucao = tk.Label(janela, text="Digite as opções separadas por vírgula:")
label_instrucao.pack(pady=10)

entrada_opcoes = tk.Entry(janela, width=50)
entrada_opcoes.pack()

# Botão
botao = tk.Button(janela, text="Girar Roleta", command=escolher_opcao)
botao.pack(pady=15)

# Resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado_var, font=("Helvetica", 16), fg="blue")
resultado_label.pack(pady=10)

# Iniciar interface
janela.mainloop()
