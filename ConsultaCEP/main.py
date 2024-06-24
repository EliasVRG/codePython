import customtkinter as ctk
import requests

# Função para consultar o CEP
def consultar():
    cep = entry_cep.get()
    api = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    
    if 'erro' not in api:
        label_result.configure(text=(
            f"CEP: {api['cep']}\n"
            f"Rua: {api['logradouro']}\n"
            f"Complemento: {api['complemento']}\n"
            f"Bairro: {api['bairro']}\n"
            f"Cidade: {api['localidade']}\n"
            f"Estado UF: {api['uf']}\n"
            f"IBGE: {api['ibge']}\n"
            f"DDD: {api['ddd']}\n"
            f"GIA: {api['gia']}\n"
        ))
        label_result_invalid.configure(text="")
    else:
        label_result.configure(text="")
        label_result_invalid.configure(text="CEP inválido")

# Função para limpar os campos
def limpar():
    entry_cep.delete(0, 'end')
    label_result.configure(text="")
    label_result_invalid.configure(text="")

# Configurações da janela principal
app = ctk.CTk()
app.title("Consulta de CEP")
app.geometry("500x500")

# Entrada de CEP
label_cep = ctk.CTkLabel(app, text="Digite o CEP:")
label_cep.pack(pady=10)

entry_cep = ctk.CTkEntry(app, width=200)
entry_cep.pack(pady=5)

# Botão de consulta
btn_consultar = ctk.CTkButton(app, text="Consultar", command=consultar)
btn_consultar.pack(pady=10)

# Área de resultado
label_result = ctk.CTkLabel(app, text="", justify="left")
label_result.pack(pady=20)

# Área de resultado inválido
label_result_invalid = ctk.CTkLabel(app, text="", justify="left")
label_result_invalid.pack(pady=5)

# Botão de limpar
btn_limpar = ctk.CTkButton(app, text="Limpar", command=limpar)
btn_limpar.pack(pady=10)

# Inicia a aplicação
app.mainloop()