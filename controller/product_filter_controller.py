import os

class ProductFilterController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_generate_command(self.generate_output)

    def generate_output(self):
        file1_lines = self.view.get_file1_lines()
        codes = self.view.get_codes()
        filtered_lines = self.model.filter_lines(file1_lines, codes)

        output_path = 'arquivo_filtrado.txt'
        self.model.write_file(output_path, filtered_lines)

        os.system(f'notepad.exe {output_path}')
