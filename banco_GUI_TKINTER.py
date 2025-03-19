#Criar uma classe que armazene as contas anteriores e criar botões que coloquem os dados das contas anteriores

import tkinter as tk

class Conta_bancaria:
    taxa_juros = 0.0
    total_contas = 0

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        Conta_bancaria.total_contas += 1

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}"
        return "Valor inválido para depósito."

    def sacar(self, valor):
        if valor <= 0:
            return "Valor inválido para saque."
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}"
        return "Saldo insuficiente."

    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):
        if nova_taxa >= 0:
            cls.taxa_juros = nova_taxa
            return f"Taxa ajustada para {nova_taxa*100}%"
        return "Taxa deve ser positiva."

    @classmethod
    def mostrar_total_contas(cls):
        return f"Total de contas: {cls.total_contas}"

conta = None
mensagem = ""

def criar_conta():
    global conta, mensagem
    titular = inp_titular.get()
    saldo = inp_saldo.get()
    
    try:
        conta = Conta_bancaria(titular, float(saldo))
        mensagem = f"Conta criada para {titular} com saldo R${float(saldo):.2f}"
        label_mensagem.config(text=mensagem)
    except:
        mensagem = "Erro ao criar conta."
        label_mensagem.config(text=mensagem)

def realizar_deposito():
    global mensagem
    if conta:
        try:
            valor = float(inp_deposito.get())
            mensagem = conta.depositar(valor)
            label_mensagem.config(text=mensagem)
        except:
            mensagem = "Valor inválido para depósito."
            label_mensagem.config(text=mensagem)
    else:
        mensagem = "Crie uma conta primeiro."
        label_mensagem.config(text=mensagem)

def realizar_saque():
    global mensagem
    if conta:
        try:
            valor = float(inp_saque.get())
            mensagem = conta.sacar(valor)
            label_mensagem.config(text=mensagem)
        except:
            mensagem = "Valor inválido para saque."
            label_mensagem.config(text=mensagem)
    else:
        mensagem = "Crie uma conta primeiro."
        label_mensagem.config(text=mensagem)

def ajustar_taxa():
    global mensagem
    try:
        valor = float(inp_taxa.get())
        mensagem = Conta_bancaria.ajustar_taxa_juros(valor)
        label_mensagem.config(text=mensagem)
    except:
        mensagem = "Valor inválido para taxa."
        label_mensagem.config(text=mensagem)

def mostrar_total_contas():
    global mensagem
    mensagem = Conta_bancaria.mostrar_total_contas()
    label_mensagem.config(text=mensagem)

root = tk.Tk()
root.title("SantGit")

tk.Label(root, text="Titular:").grid(row=0, column=0)
root.config(bg="red")
inp_titular = tk.Entry(root)
inp_titular.grid(row=0, column=1)

tk.Label(root, text="Saldo Inicial:").grid(row=1, column=0)
inp_saldo = tk.Entry(root)
inp_saldo.grid(row=1, column=1)

tk.Button(root, text="Criar Conta", command=criar_conta).grid(row=2, column=0, columnspan=2)

tk.Label(root, text="Depósito (R$):").grid(row=3, column=0)
inp_deposito = tk.Entry(root)
inp_deposito.grid(row=3, column=1)
tk.Button(root, text="Depositar", command=realizar_deposito).grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Saque (R$):").grid(row=5, column=0)
inp_saque = tk.Entry(root)
inp_saque.grid(row=5, column=1)
tk.Button(root, text="Sacar", command=realizar_saque).grid(row=6, column=0, columnspan=2)

tk.Label(root, text="Nova Taxa (%):").grid(row=7, column=0)
inp_taxa = tk.Entry(root)
inp_taxa.grid(row=7, column=1)
tk.Button(root, text="Ajustar Taxa", command=ajustar_taxa).grid(row=8, column=0, columnspan=2)

tk.Button(root, text="Ver Total de Contas", command=mostrar_total_contas).grid(row=9, column=0, columnspan=2)

label_mensagem = tk.Label(root, text="")
label_mensagem.grid(row=10, column=0, columnspan=2)

from PIL import Image, ImageTk

img = Image.open("santgit.png")
img_tk = ImageTk.PhotoImage(img)

label_imagem = tk.Label(root, image=img_tk, bg="red")
label_imagem.image = img_tk
label_imagem.grid(row=11, column=0, columnspan=2)

root.mainloop()