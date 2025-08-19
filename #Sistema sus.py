#Sistema sus 
import tkinter as tk
from tkinter import *
from tkinter import ttk

COR_FUNDO = "#0D0F13"
sintomas = ["Febre", "Dor de cabeça", "Tristeza", "Dor de barriga", "DOR MUITO FORTE"]

root = Tk()
root.configure(background="white")
root.title("SISTEMA DO SUS")
root.configure(background="white")
root.geometry("400x300")
# Corrigindo a criação do frame
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)


label_sus = ttk.Label(frame, text="Sistema SUS", font=("Helvetica", 16, "bold"), background=COR_FUNDO, foreground="black")
label_sus.pack(pady=10)
tk.Label(frame, text="Bem-vindo ao Sistema SUS", font=("Helvetica", 18, "bold"), foreground="black").pack(pady=10)
tk.Label(frame, text="Selecione o oque vc está sentindo ? diga seu sintoma:", foreground="black").pack(pady=10)

# Combobox para seleção de sintomas
sintoma_var = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=sintoma_var, values=sintomas, state="readonly")
combobox.pack(pady=10)

# Função para mostrar resultado baseado no sintoma selecionado
def escolher_sintoma():
    sintoma = sintoma_var.get()
    if sintoma == "Febre":
        resultado.config(text="Vai tomar dipirona")
    elif sintoma == "Dor de cabeça":
        resultado.config(text="Vai tomar dipirona")
    elif sintoma == "Tristeza":
        resultado.config(text="Tá com depressão e vai tomar dipirona")
    elif sintoma == "Dor de barriga":
        resultado.config(text="Vai tomar dipirona")
    elif sintoma == "DOR MUITO FORTE":
        resultado.config(text="Vai tomar Benzetacil")
    else:
        resultado.config(text="Selecione um sintoma.")

# Botão para executar a função
botao = ttk.Button(frame, text="Verificar", command=escolher_sintoma)
botao.pack(pady=10)

# Label para mostrar o resultado
resultado = ttk.Label(frame, text="")
resultado.pack(pady=10)

sus_resultado = ttk.Label(frame, text="O SUS AGRADECE, JUNTOS VAMOS SALVAR VIDAS", background=COR_FUNDO, foreground="white")
root.mainloop()
tk.Frame()