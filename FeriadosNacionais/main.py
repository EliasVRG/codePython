from datetime import datetime
import requests
import tkinter as tk
from tkinter import messagebox

def consultar_feriados():
    ano = entry_ano.get()

    if not ano.isdigit():
        messagebox.showerror("Erro", "Por favor, digite um ano válido.")
        return

    try:
        feriados_futuros = get_feriados(int(ano))
        exibir_feriados(feriados_futuros)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar feriados: {str(e)}")

def get_feriados(ano):
    feriados_url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    response = requests.get(feriados_url)

    if response.status_code != 200:
        raise Exception("Erro ao buscar feriados")

    feriados = response.json()
    data_atual = datetime.now().date()

    # Filtra os feriados que ainda vão acontecer
    feriados_futuros = [feriado for feriado in feriados if datetime.strptime(feriado["date"], "%Y-%m-%d").date() >= data_atual]

    return feriados_futuros

def exibir_feriados(feriados):
    text_feriados.config(state=tk.NORMAL)
    text_feriados.delete("1.0", tk.END)

    if not feriados:
        text_feriados.insert(tk.END, "Não há feriados futuros para o ano informado.")
    else:
        for feriado in feriados:
            text_feriados.insert(tk.END, f"{feriado['name']} - {feriado['date']}\n")

    text_feriados.config(state=tk.DISABLED)

# Configuração da interface gráfica com tkinter
root = tk.Tk()
root.title("Consulta de Feriados")
root.geometry("600x400")

# Cor de fundo e fonte para a interface
root.configure(bg="#4a3a47")
label_ano = tk.Label(root, text="Digite o ano para consultar:", fg="white", bg="#4a3a47", font=("Montserrat", 14))
label_ano.pack(pady=20)

entry_ano = tk.Entry(root, width=15, font=("Arial", 14))
entry_ano.pack()

button_consultar = tk.Button(root, text="Consultar", command=consultar_feriados, font=("Montserrat", 14), bg="#4a3a50", fg="white")
button_consultar.pack(pady=20)

text_feriados = tk.Text(root, width=50, height=10, wrap=tk.WORD, font=("Montserrat", 12), bd=2, relief=tk.SOLID)
text_feriados.pack(padx=10, pady=10)
text_feriados.config(state=tk.DISABLED)

root.mainloop()
