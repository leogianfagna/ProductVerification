class ProductFilterModel:
    def read_text_from_input(self, text_widget):
        return text_widget.get("1.0", "end").strip().splitlines()

    def write_file(self, file_path, lines):
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + "\n")

    def filter_lines(self, file1_lines, codes):
        return [line for line in file1_lines if line.split()[0] in codes]
