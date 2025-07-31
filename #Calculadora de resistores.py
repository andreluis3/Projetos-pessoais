import tkinter as tk
from tkinter import ttk

# Dicionários
dic_resistores = {
    "preto": 0, "marrom": 1, "vermelho": 2, "laranja": 3,
    "amarelo": 4, "verde": 5, "azul": 6, "violeta": 7,
    "cinza": 8, "branco": 9
}

tipo_resistor = {
    "3 bandas": 3, "4 bandas": 4, "5 bandas": 5
}

n_zeros_multiplicador = {
    "preto": 0, "marrom": 1, "vermelho": 2, "laranja": 3,
    "amarelo": 4, "verde": 5, "azul": 6, "violeta": 7,
    "cinza": 8, "branco": 9, "dourado": -1, "prata": -2
}

tolerancia_dic = {
    "marrom": 0.01, "vermelho": 0.02, "verde": 0.005,
    "azul": 0.0025, "violeta": 0.001, "cinza": 0.0005,
    "dourado": 0.05, "prata": 0.1
}

color_map = {
    "preto": "black", "marrom": "#5A2D0C", "vermelho": "red", "laranja": "orange",
    "amarelo": "yellow", "verde": "green", "azul": "blue", "violeta": "purple",
    "cinza": "gray", "branco": "white", "dourado": "#D4AF37", "prata": "light gray"
}

# Funções
# 1e9 == 1 * 10^9 == 1.000.000.000
def conversor_de_ohmns(valor):
    if valor >= 1e9:
        return f"{valor / 1e9:.2f} GΩ"
    elif valor >= 1e6:
        return f"{valor / 1e6:.2f} MΩ"
    elif valor >= 1e3:
        return f"{valor / 1e3:.2f} kΩ"
    else:
        return f"{valor:.2f} Ω"

def atualizar_campos(*args):
    tipo = tipo_var.get()
    if tipo == "5 bandas":
        cor4_frame.grid()
    else:
        cor4_frame.grid_remove()

def mostrar_cor(cor, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    if cor:
        tk.Frame(frame, bg=color_map.get(cor, "white"), width=30, height=30).pack()

def calcular_resistor():
    try:
        cor1 = dic_resistores[cor1_var.get()]
        cor2 = dic_resistores[cor2_var.get()]
        cor3 = dic_resistores[cor3_var.get()]
        tipo = tipo_resistor[tipo_var.get()]
        if tipo == 3:
            valor = (cor1 * 10 + cor2) * (10 ** cor3)
        elif tipo == 4:
            valor = (cor1 * 10 + cor2) * (10 ** n_zeros_multiplicador[cor3_var.get()])
        elif tipo == 5:
            cor4 = cor4_var.get()
            valor = (cor1 * 100 + cor2 * 10 + cor3) * (10 ** n_zeros_multiplicador[cor4])
        tolerancia = tolerancia_dic[tolerancia_var.get()]
        resultado.set(f"Valor: {conversor_de_ohmns(valor)} ± {tolerancia*100}%")
        desenhar_resistor()
    except:
        resultado.set("Erro: Verifique as cores selecionadas.")

def desenhar_resistor():
    canvas.delete("all")
    canvas.create_rectangle(50, 60, 250, 100, fill="#F5DEB3", outline="black", width=2)
    canvas.create_line(0, 80, 50, 80, width=5)
    canvas.create_line(250, 80, 300, 80, width=5)
    
    faixas = [cor1_var.get(), cor2_var.get(), cor3_var.get()]
    if tipo_var.get() == "5 bandas":
        faixas.append(cor4_var.get())
    faixas.append(tolerancia_var.get())

    posicoes = [80, 110, 140, 170, 200]
    
    for i, cor in enumerate(faixas):
        if cor:
            canvas.create_rectangle(50 + posicoes[i], 60, 60 + posicoes[i], 100, fill=color_map.get(cor, "white"), outline="black")

# Interface
janela = tk.Tk()
janela.title("Calculadora de Resistores")
janela.geometry("400x550")

# Variáveis
cor1_var = tk.StringVar()
cor2_var = tk.StringVar()
cor3_var = tk.StringVar()
cor4_var = tk.StringVar()
tipo_var = tk.StringVar(value="4 bandas")
tolerancia_var = tk.StringVar()
resultado = tk.StringVar()

main_frame = ttk.Frame(janela, padding=10)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Tipo de resistor:").pack()
tipo_combo = ttk.Combobox(main_frame, textvariable=tipo_var, values=list(tipo_resistor.keys()), state="readonly")
tipo_combo.pack()
tipo_combo.bind("<<ComboboxSelected>>", atualizar_campos)

# Função para criar os frames de cor
def criar_frame_cor(label, var, dic):
    frame = ttk.Frame(main_frame)
    frame.pack(pady=5)
    ttk.Label(frame, text=label).pack(side="left")
    combo = ttk.Combobox(frame, textvariable=var, values=list(dic.keys()), state="readonly")
    combo.pack(side="left")
    cor_display = ttk.Frame(frame)
    cor_display.pack(side="left", padx=10)
    var.trace("w", lambda *args: mostrar_cor(var.get(), cor_display))
    return frame

cor1_frame = criar_frame_cor("Cor 1:", cor1_var, dic_resistores)
cor2_frame = criar_frame_cor("Cor 2:", cor2_var, dic_resistores)
cor3_frame = criar_frame_cor("Cor 3 (Multiplicador):", cor3_var, n_zeros_multiplicador)
cor4_frame = criar_frame_cor("Cor 4 (5 bandas):", cor4_var, n_zeros_multiplicador)

# Tolerância
tol_frame = ttk.Frame(main_frame)
tol_frame.pack(pady=5)
ttk.Label(tol_frame, text="Tolerância:").pack(side="left")
tolerancia_combo = ttk.Combobox(tol_frame, textvariable=tolerancia_var, values=list(tolerancia_dic.keys()), state="readonly")
tolerancia_combo.pack(side="left")

# Botão calcular
ttk.Button(main_frame, text="Calcular", command=calcular_resistor).pack(pady=10)

# Resultado
ttk.Label(main_frame, textvariable=resultado, font=("Arial", 12)).pack()

# Canvas
canvas = tk.Canvas(janela, width=300, height=150, bg="white")
canvas.pack(pady=10)

# Inicializa com os campos corretos
atualizar_campos()

janela.mainloop()
