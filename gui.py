import tkinter as tk
from tkinter import messagebox
import os
from logic import filter_lines, write_file
import database as db

def generate_output(text_area_file1, text_area_file2):
    # Lê entradas e salva no banco de dados
    estoque_lines = text_area_file1.get("1.0", tk.END).strip().splitlines()
    solicitados_lines = text_area_file2.get("1.0", tk.END).strip().splitlines()

    # Armazena no banco
    for line in estoque_lines:
        if line.strip():
            parts = line.strip().split(maxsplit=1)
            codigo = parts[0]
            descricao = parts[1] if len(parts) > 1 else ""
            db.insert_estoque(codigo, descricao)

    for codigo in solicitados_lines:
        if codigo.strip():
            db.insert_solicitado(codigo.strip())

    estoque = db.get_estoque()
    solicitados = set(db.get_solicitados())

    filtrados = filter_lines(estoque, solicitados)
    path = 'data/arquivo_filtrado.txt'
    write_file(path, filtrados)

    os.system(f'notepad.exe {path}')
    messagebox.showinfo("Sucesso", "Arquivo gerado com sucesso!")

def start_gui():
    root = tk.Tk()
    root.title("Sistema de verificação de produtos")
    root.geometry("1200x800")

    label1 = tk.Label(root, text="Tabela de estoque da empresa:")
    label1.pack()
    text1 = tk.Text(root, height=20, width=160)
    text1.pack()

    label2 = tk.Label(root, text="Código (material) dos produtos solicitados:")
    label2.pack()
    text2 = tk.Text(root, height=20, width=160)
    text2.pack()

    btn = tk.Button(root, text="Filtrar produtos", command=lambda: generate_output(text1, text2))
    btn.pack()

    root.mainloop()
