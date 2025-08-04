# CALCULADORA DE CAGADA REMUNERADA

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pillow as PIL
COR_FUNDO = "#0D0F13"

# Função de cálculo
def calcular():
    try:
        # Coleta de dados
        remuneracao = float(entry_remuneracao.get())
        jornada = float(entry_jornada.get())
        tc = float(entry_tc.get())

        # Cálculos
        rd = remuneracao / 30               # remuneração diária
        r_h = rd / jornada                  # remuneração por hora
        r_m = r_h / 60                      # remuneração por minuto
        cr = tc * r_m                       # valor da cagada

        # Resultado
        label_resultado.config(text=f"💩 Valor da Cagada Remunerada: R$ {cr:.2f}")

    except ValueError:
        label_resultado.config(text="❌ Insira apenas valores numéricos.")

# Criação da interface
app = ttk.Window(title="Calculadora de Cagada Remunerada", themename="darkly", size=(400, 350))

# Título
ttk.Label(app, text="Calculadora de Cagada Remunerada", font=("Helvetica", 19, "bold")).pack(pady=10)

frame_principal = ttk.Frame(app, bootstyle=SECONDARY)
frame_principal.place(relwidth=1, relheight=1)
frame_principal.configure(style="Fundo.TFrame")

# Personaliza o estilo do frame
style = ttk.Style()
style.configure("Fundo.TFrame", background=COR_FUNDO)
# Labels e entradas
ttk.Label(app, text="💼 Remuneração Mensal (R$):").pack(pady=5)
entry_remuneracao = ttk.Entry(app)
entry_remuneracao.pack()

ttk.Label(app, text="🕗 Jornada Diária (horas):").pack(pady=5)
entry_jornada = ttk.Entry(app)
entry_jornada.pack()

ttk.Label(app, text="⏱️ Tempo da Cagada (minutos):").pack(pady=5)
entry_tc = ttk.Entry(app)
entry_tc.pack()

# Botão de cálculo
ttk.Button(app, text="Calcular", command=calcular, bootstyle=SUCCESS).pack(pady=20)

# Label de resultado
label_resultado = ttk.Label(app, text="", font=("Helvetica", 12, "bold"))
label_resultado.pack(pady=10)

# Inicia o app
app.mainloop()
