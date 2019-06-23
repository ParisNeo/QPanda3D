from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

H=Qt.__dict__
lst = [a for a in H if a.startswith("Key_")]
QPanda3D_Key_translation ="QPanda3D_Key_translation ={"
for i in range(len(lst)):
    QPanda3D_Key_translation  +="Qt.{}:'unknown',\n".format(lst[i])
QPanda3D_Key_translation += "}"
print(QPanda3D_Key_translation)