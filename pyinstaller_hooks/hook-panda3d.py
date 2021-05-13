# A hook for qpanda3d
# Author : Saifeddine ALOUI
# Description : A hook to enable compiling a QPanda3d app using Pyinstaller
# Please refer to /doc/build_project_using_pyinstaller.md
# Notice, this hook can also be used to build a panda3d app using pyinstaller

from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_dynamic_libs

print(" -------- Adding panda3d hook ------------")

hiddenimports = collect_submodules('panda3d')
datas = collect_data_files('panda3d')
binaries = collect_dynamic_libs('panda3d')