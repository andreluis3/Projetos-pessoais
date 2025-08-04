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
import matplotlib.pyplot as plt
import pandas as pd

def exibir_cagadas():
    # Janela secundária
    janela = ttk.Toplevel(title="Cagadas Registradas", themename="darkly")
    janela.geometry("700x500")

    # ==================== TABELA TREEVIEW ====================
    tree = ttk.Treeview(janela, columns=("tempo", "valor", "data", "mes", "dia"), show="headings", height=15)
    tree.heading("tempo", text="Tempo (min)")
    tree.heading("valor", text="Valor R$")
    tree.heading("data", text="Data e Hora")
    tree.heading("mes", text="Mês")
    tree.heading("dia", text="Dia da Semana")

    tree.column("tempo", anchor="center", width=100)
    tree.column("valor", anchor="center", width=100)
    tree.column("data", anchor="center", width=200)
    tree.column("mes", anchor="center", width=100)
    tree.column("dia", anchor="center", width=100)

    tree.pack(pady=10, padx=10, fill="both", expand=True)

    # ==================== LER DO BANCO ====================
    conn = sqlite3.connect("cagadas.db")
    df = pd.read_sql_query("SELECT * FROM cagadas", conn)
    conn.close()

    for _, row in df.iterrows():
        tree.insert("", "end", values=(row["tempo"], f"{row['valor']:.2f}", row["data_hora"], row["mes"], row["dia_semana"]))

    # ==================== GRÁFICOS ====================
    def mostrar_graficos():
        if df.empty:
            return

        # -------- Gráfico 1: Mês que mais cagou e ganhou --------
        df_mes = df.groupby("mes").agg({"tempo": "sum", "valor": "sum"}).sort_values("tempo", ascending=False)

        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        plt.bar(df_mes.index, df_mes["tempo"], color='brown')
        plt.title("Tempo total de Cagada por Mês (min)")
        plt.xticks(rotation=45)

        plt.subplot(1, 2, 2)
        plt.bar(df_mes.index, df_mes["valor"], color='green')
        plt.title("Dinheiro Ganho Cagando por Mês (R$)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # -------- Gráfico 2: Tempo de Cagada vs Tempo Trabalhado --------
        tempo_total_cagada = df["tempo"].sum()
        tempo_trabalho_mensal = 30 * float(entry_jornada.get())

        plt.figure(figsize=(5, 5))
        plt.pie(
            [tempo_total_cagada, tempo_trabalho_mensal - tempo_total_cagada],
            labels=["Tempo Cagando", "Tempo Trabalhando"],
            colors=["orange", "blue"],
            autopct="%1.1f%%"
        )
        plt.title("Proporção do Tempo no Mês")
        plt.show()

        # -------- Gráfico 3: Dinheiro cagando vs dinheiro total --------
        valor_cagando = df["valor"].sum()
        valor_total = float(entry_remuneracao.get())

        plt.figure(figsize=(5, 5))
        plt.pie(
            [valor_cagando, valor_total - valor_cagando],
            labels=["💩 Cagando", "💼 Trabalhando"],
            colors=["green", "gray"],
            autopct="%1.1f%%"
        )
        plt.title("Remuneração Cagando vs Trabalhando")
        plt.show()

    # Botão mostrar gráficos
    ttk.Button(janela, text="📊 Mostrar Gráficos", command=mostrar_graficos, bootstyle=INFO).pack(pady=10)



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
img_titulo = img_titulo.resize((450, 200))
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


img_cj = Image.open(r"C:\Users\André Luis\Documents\Alg criados por mim\Projetos\Projetos-pessoais\calculadoracagada\cj.png")
img_cj = img_cj.resize((200, 200))
img_cj_tk = ImageTk.PhotoImage(img_cj)
ttk.Label(frame, image=img_cj_tk, background=COR_FUNDO).pack(side="bottom", pady=10)

criar_banco()
app.mainloop()
