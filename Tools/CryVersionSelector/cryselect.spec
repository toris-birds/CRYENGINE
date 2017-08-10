# -*- mode: python -*-

block_cipher = None


a = Analysis(['cryselect.py', 'cryproject.py', 'cryregistry.py'],
             pathex=['CryVersionSelector'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='cryselect',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='editor_icon16.ico')
