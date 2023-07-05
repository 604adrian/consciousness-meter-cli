# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('./2end_credits_head.sh', '.'),
        ('./2illusionist.sh', '.'),
        ('./2panpsychist.sh', '.'),
        ('./animation.sh', '.'),
        ('./animation2.sh', '.'),
        ('./bar.sh', '.'),
        ('./booting.sh', '.'),
        ('./closing_ani.sh', '.'),
        ('./end_credits_head.sh', '.'),
        ('./illusionist.sh', '.'),
        ('./menu.sh', '.'),
        ('./panpsychist.sh', '.'),
        ('./second_menu.sh', '.'),
        ('./shut_down.sh', '.'),
        ('./third_menu.sh', '.'),
        ('./antipat.mp3', '.'),
        ('./bach.mp3', '.'),
        ('./beep.mp3', '.'),
        ('./button.mp3', '.'),
        ('./conscious.mp3', '.'),
        ('./not_conscious.mp3', '.'),
        ('./shutdown.mp3', '.'),
        ('./ufo.wav', '.'),
        ('./beep.ogg', '.'),
        ('./credits.txt', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
