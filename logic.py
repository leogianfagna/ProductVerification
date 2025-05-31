def filter_lines(estoque, solicitados):
    return [f"{codigo} {descricao}" for codigo, descricao in estoque if codigo in solicitados]

def write_file(path, lines):
    with open(path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + "\n")
