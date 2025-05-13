import tkinter as tk
from tkinter import messagebox
import os

def read_text_from_input(text_widget):
    return text_widget.get("1.0", tk.END).strip().splitlines()

def write_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + "\n")

def filter_lines(file1_lines, codes):
    filtered_lines = []
    for line in file1_lines:
        code = line.split()[0]
        if code in codes:
            filtered_lines.append(line)
    return filtered_lines

def generate_output():
    file1_lines = read_text_from_input(text_area_file1)
    codes = set(read_text_from_input(text_area_file2))
    filtered_lines = filter_lines(file1_lines, codes)
    output_path = 'arquivo_filtrado.txt'
    write_file(output_path, filtered_lines)
    
    # Abre o arquivo gerado com o bloco de notas padrão do Windows
    os.system(f'notepad.exe {output_path}')

# Configuração da interface gráfica
root = tk.Tk()
root.title("Sistema de verificação de protudos")
root.geometry("1200x800")

# Área de texto para o primeiro arquivo
label_file1 = tk.Label(root, text="Tabela de estoque da empresa:")
label_file1.pack()
text_area_file1 = tk.Text(root, height=20, width=160)
text_area_file1.pack()

# Área de texto para o segundo arquivo
label_file2 = tk.Label(root, text="Código (material) dos produtos solicitados:")
label_file2.pack()
text_area_file2 = tk.Text(root, height=20, width=160)
text_area_file2.pack()

# Botão para gerar o arquivo de saída
generate_button = tk.Button(root, text="Filtrar produtos", command=generate_output)
generate_button.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
