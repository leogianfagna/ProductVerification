# Funcionalidade
Programada criado para filtrar os materiais em estoque que foram solicitados por um cliente, gerando uma tabela final informativa com os itens em comum entre solicitado e em estoque pela empresa.

# Como usar
Instale o programa [aqui](https://github.com/MathMSilva/Sistema-de-Verifica-o-de-Produto/releases), basta baixar e executá-lo, é um programa muito leve que não exige o Python instalado. Ao abrir, cole na primeira lacuna um CTROL + C da tabela excel do seu estoque e na segunda lacuna um CTROL C dos códigos referentes aos materiais solicitados pelo cliente, assim como está na foto abaixo:

![image](https://github.com/user-attachments/assets/fd96fe68-eb41-4efc-bc41-f3552b3be40a)

Em seguida, faça a busca e tenha em um bloco de notas o resultado. Você pode salvar esse arquivo, assim como editar. Sinta-se livre! 

# Build
1. Clonar o repositório
2. Instalar a extensão [Pyinstaller](https://pyinstaller.org/en/v3.4/installation.html)
3. Executar no terminal do diretório: `pyinstaller --onefile comparar_produtos.py`
