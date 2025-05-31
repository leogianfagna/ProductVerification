import tkinter as tk

class ProductFilterView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de verificação de produtos")
        self.root.geometry("1200x800")

        self.label_file1 = tk.Label(root, text="Tabela de estoque da empresa:")
        self.label_file1.pack()
        self.text_area_file1 = tk.Text(root, height=20, width=160)
        self.text_area_file1.pack()

        self.label_file2 = tk.Label(root, text="Código (material) dos produtos solicitados:")
        self.label_file2.pack()
        self.text_area_file2 = tk.Text(root, height=20, width=160)
        self.text_area_file2.pack()

        self.generate_button = tk.Button(root, text="Filtrar produtos")
        self.generate_button.pack()

    def set_generate_command(self, command):
        self.generate_button.config(command=command)

    def get_file1_lines(self):
        return self.text_area_file1.get("1.0", "end").strip().splitlines()

    def get_codes(self):
        return set(self.text_area_file2.get("1.0", "end").strip().splitlines())
