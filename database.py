import sqlite3
import random

DB_NAME = "produtos.db"


def importar_estoque_de_txt(caminho_arquivo='exemplos/produtos_estoque.txt'):
    import os
    if not os.path.exists(caminho_arquivo):
        print(f"[ERRO] Arquivo '{caminho_arquivo}' não encontrado.")
        return

    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        if not linhas:
            print("[AVISO] Arquivo está vazio.")
            return

        for linha in linhas[1:]:  # pula o cabeçalho
            partes = linha.strip().split('\t')
            if len(partes) >= 2:
                codigo = partes[0].strip()
                descricao = partes[1].strip()
                insert_estoque(codigo, descricao)
        print(f"{len(linhas)-1} itens importados para a tabela 'estoque'.")


def connect():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS estoque (
            codigo TEXT PRIMARY KEY,
            descricao TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS solicitados (
            codigo TEXT PRIMARY KEY
        )
    ''')
    conn.commit()
    return conn

def insert_estoque(codigo, descricao):
    conn = connect()
    cur = conn.cursor()
    cur.execute('INSERT OR REPLACE INTO estoque VALUES (?, ?)', (codigo, descricao))
    conn.commit()
    conn.close()

def insert_solicitado(codigo):
    conn = connect()
    cur = conn.cursor()
    cur.execute('INSERT OR REPLACE INTO solicitados VALUES (?)', (codigo,))
    conn.commit()
    conn.close()

def get_estoque():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM estoque')
    rows = cur.fetchall()
    conn.close()
    return rows

def get_solicitados():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT codigo FROM solicitados')
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return rows
