# CALCULADORA DE CAGADA REMUNERADA

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
COR_FUNDO = "#0D0F13"

# (Removed duplicate/unused code and interface creation)
import sqlite3
from datetime import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

# ========================== BANCO DE DADOS ================================
def criar_banco():
    conn = sqlite3.connect("cagadas.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cagadas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tempo REAL,
            valor REAL,
            data_hora TEXT,
            mes TEXT,
            dia_semana TEXT
        )
    ''')
    conn.commit()
    conn.close()

# =========================== CÁLCULO + REGISTRO ===========================
def calcular_e_registrar():
    try:
        remuneracao = float(entry_remuneracao.get())
        jornada = float(entry_jornada.get())
        tc = float(entry_tc.get())

        rd = remuneracao / 30
        r_h = rd / jornada
        r_m = r_h / 60
        cr = tc * r_m

        agora = datetime.now()
        data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")
        mes = agora.strftime("%B")
        dia_semana = agora.strftime("%A")

        # Inserir no banco
        conn = sqlite3.connect("cagadas.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cagadas (tempo, valor, data_hora, mes, dia_semana)
            VALUES (?, ?, ?, ?, ?)
        ''', (tc, cr, data_hora, mes, dia_semana))
        conn.commit()
        conn.close()

        label_resultado.config(text=f"✅ Cagada registrada: R$ {cr:.2f}")

    except ValueError:
        label_resultado.config(text="❌ Insira apenas valores numéricos.")

# ============================== INTERFACE ================================
COR_FUNDO = "#0D0F13"

app = ttk.Window(title="Calculadora de Cagada Remunerada", themename="darkly", size=(500, 650))
frame = ttk.Frame(app, bootstyle=SECONDARY)
frame.place(relwidth=1, relheight=1)
frame.configure(style="Fundo.TFrame")
style = ttk.Style()
style.configure("Fundo.TFrame", background=COR_FUNDO)

# ============================== IMAGENS ================================
# Imagem do título
img_titulo = Image.open(r"C:\Users\André Luis\Documents\Alg criados por mim\Projetos\Projetos-pessoais\calculadoracagada\hora.png")
img_titulo = img_titulo.resize((350, 100))
img_titulo_tk = ImageTk.PhotoImage(img_titulo)
ttk.Label(frame, image=img_titulo_tk, background=COR_FUNDO, justify='center').pack(pady=(10, 5))


ttk.Label(frame, text="💼 Remuneração Mensal (R$):", background=COR_FUNDO, foreground="white").pack(pady=5)
entry_remuneracao = ttk.Entry(frame)
entry_remuneracao.pack()

ttk.Label(frame, text="🕗 Jornada Diária (horas):", background=COR_FUNDO, foreground="white").pack(pady=5)
entry_jornada = ttk.Entry(frame)
entry_jornada.pack()

ttk.Label(frame, text="⏱️ Tempo da Cagada (minutos):", background=COR_FUNDO, foreground="white").pack(pady=5)
entry_tc = ttk.Entry(frame)
entry_tc.pack()

#botao registrar cagada
ttk.Button(frame, text="Registrar Cagada", command=calcular_e_registrar, bootstyle=SUCCESS).pack(pady=20)

label_resultado = ttk.Label(frame, text="", font=("Helvetica", 12, "bold"), background=COR_FUNDO, foreground="white")
label_resultado.pack(pady=10)


img_cj = Image.open("C:\Users\André Luis\Documents\Alg criados por mim\Projetos\Projetos-pessoais\calculadoracagada\cj.png")
img_cj = img_cj.resize((100, 100))
img_cj_tk = ImageTk.PhotoImage(img_cj)
ttk.Label(frame, image=img_cj_tk, background=COR_FUNDO).pack(side="bottom", pady=10)

criar_banco()
app.mainloop()
