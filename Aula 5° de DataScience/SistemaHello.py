# desenha tela GUI (Graphical User Interface)

import tkinter as tk
from tkinter import messagebox

def mostrarMensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Saudação", f"Olá, {nome}, bem-vindo!")

# criando janela 
janela = tk.Tk()
janela.title("Olá Tkinter")
janela.geometry("300x150")

# criando label do input
rotulo_nome = tk.Label(janela, text="Digite o seu nome:")
rotulo_nome.pack(padx=5)

# criando campo de entrada
entrada_nome = tk.Entry(janela)
entrada_nome.pack(padx=5)

# criando botão
botao = tk.Button(janela, text="Clique aqui", command=mostrarMensagem)
botao.pack(pady=20)

janela.mainloop()
