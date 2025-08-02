import tkinter as tk
from tkinter import messagebox
import csv
import os
import re

# ─── Funções de validação ───────────────────────────────────────────────

def validar_nome(novo_texto: str) -> bool:
    """
    Permite apenas letras (maiúsculas/minúsculas). Permite apagar tudo (texto vazio).
    """
    return novo_texto == "" or novo_texto.isalpha()

def validar_nota(novo_texto: str) -> bool:
    """
    Permite apenas dígitos e até um ponto decimal, com no máximo um '.'.
    Não impõe o intervalo aqui (ou seja, permite 11.5 ao digitar), 
    mas evita letras. O intervalo é conferido no botão.
    """
    # Regex: opcional sinais +, −; apenas dígitos e ponto; no máximo um ponto
    return bool(re.fullmatch(r"[0-9]*\.?[0-9]*", novo_texto))

# ─── Função para salvar em CSV ───────────────────────────────────────────

def salvar_em_csv(nome: str, nota: float):
    arquivo = 'dados.csv'
    existe = os.path.isfile(arquivo)
    with open(arquivo, mode='a', newline='', encoding='utf‑8') as f:
        escritor = csv.writer(f)
        if not existe:
            escritor.writerow(['Nome', 'Nota'])
        escritor.writerow([nome, f"{nota:.2f}"])

# ─── Fluxo de janelas ──────────────────────────────────────────────────

def mostrarMensagemNome():
    nome = entrada_nome.get().strip()
    if nome == "":
        messagebox.showwarning("Atenção", "Informe seu nome.")
        return
    messagebox.showinfo("Saudação", f"Olá, {nome}!")
    # Exibe os campos da nota
    rotulo_nota.pack(padx=5); entrada_nota.pack(padx=5); botao_nota.pack(pady=10)

def mostrarMensagemNota():
    nome = entrada_nome.get().strip()
    txt_nota = entrada_nota.get().strip()
    if txt_nota == "":
        messagebox.showwarning("Atenção", "Informe sua nota (0 a 10).")
        return
    try:
        nota = float(txt_nota)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para a nota.")
        entrada_nota.focus_set()
        return
    if nota < 0 or nota > 10:
        messagebox.showerror("Erro", "A nota deve ser entre 0 e 10.")
        entrada_nota.focus_set()
        return

    # Mensagem final + salva dados
    if nota <= 5:
        messagebox.showinfo("Resultado", "Nota abaixo da média.")
    else:
        messagebox.showinfo("Resultado", "Parabéns! Nota excelente.")
    salvar_em_csv(nome, nota)
    # limpa os campos para nova entrada
    entrada_nome.delete(0, tk.END)
    entrada_nota.delete(0, tk.END)
    entrada_nome.focus_set()

# ─── Criação da janela ──────────────────────────────────────────────────

root = tk.Tk()
root.title("Cadastro de Notas")
root.geometry("300x260")

# Registra as funções para o Tcl do Tkinter
vc_nome = root.register(validar_nome)
vc_nota = root.register(validar_nota)

# Widgets — Nome
tk.Label(root, text="Digite o seu nome:").pack(padx=5, pady=(10,0))
entrada_nome = tk.Entry(root, validate="key", validatecommand=(vc_nome, "%P"))
entrada_nome.pack(padx=5)
tk.Button(root, text="Saudar", command=mostrarMensagemNome).pack(pady=10)

# Widgets — Nota (inicialmente ocultos)
rotulo_nota = tk.Label(root, text="Digite sua nota (0‑10):")
entrada_nota = tk.Entry(root, validate="key", validatecommand=(vc_nota, "%P"))
botao_nota = tk.Button(root, text="Verificar Nota", command=mostrarMensagemNota)

# Define o foco inicial
entrada_nome.focus_set()
root.mainloop()
