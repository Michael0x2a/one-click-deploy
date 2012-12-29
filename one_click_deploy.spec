# -*- mode: python -*-
a = Analysis(['one_click_deploy.pyw'],
             pathex=['C:\\Users\\Michael\\Dropbox\\Projects\\Robotics\\Tools\\one-click-deploy'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'one_click_deploy.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='resources\\icon.ico')
app = BUNDLE(exe,
             name=os.path.join('dist', 'one_click_deploy.exe.app'))
