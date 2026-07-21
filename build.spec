# -*- mode: python ; coding: utf-8 -*-
# Fichier de build PyInstaller pour CathLab Manager v1.0
# Utilisation (sur Windows, dans un venv avec les dependances installees) :
#     pyinstaller build.spec
# Le .exe est genere dans dist/CathLabManager/CathLabManager.exe

import customtkinter
from pathlib import Path

ctk_path = Path(customtkinter.__file__).parent

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (str(ctk_path), 'customtkinter'),
        ('assets', 'assets'),
    ],
    hiddenimports=['tkcalendar', 'babel.numbers'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CathLabManager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CathLabManager',
)
