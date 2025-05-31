# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],  # <-- ponto de entrada correto agora
    pathex=[],
    binaries=[],
    datas=[
      
        ('exemplo/produtos_estoque.txt', 'exemplo'),  # Inclui arquivos de exemplo
        ('exemplo/produtos_solicitados.txt', 'exemplo'),
    ],
    hiddenimports=['tkinter', 'sqlite3'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='comparar_produtos_gui',  # você pode trocar para outro nome se quiser
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # False = GUI (tkinter). Use True se quiser ver erros em terminal.
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
