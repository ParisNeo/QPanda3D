# -*- coding: utf-8-*-
"""
Module : QPanda3D_Translation_Buttons
Author : Niklas Mevenkamp
Description :
    Contains a dictionary that translates QT mouse events to panda3d
    mouse events.
"""
# PyQt imports
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
__all__ = ["QPanda3D_Keys_Translation"]

QPanda3D_Button_translation ={
Qt.MouseButton.NoButton:'',
Qt.MouseButton.AllButtons:'unknown',
Qt.MouseButton.LeftButton:'mouse1',
Qt.MouseButton.RightButton:'mouse2',
Qt.MouseButton.MiddleButton:'mouse3',
Qt.MouseButton.BackButton:'unknown',
Qt.MouseButton.XButton1:'unknown',
Qt.MouseButton.ExtraButton1:'unknown',
Qt.MouseButton.ForwardButton:'unknown',
Qt.MouseButton.XButton2:'unknown',
Qt.MouseButton.ExtraButton2:'unknown',
Qt.MouseButton.TaskButton:'unknown',
Qt.MouseButton.ExtraButton3:'unknown',
Qt.MouseButton.ExtraButton4:'unknown',
Qt.MouseButton.ExtraButton5:'unknown',
Qt.MouseButton.ExtraButton6:'unknown',
Qt.MouseButton.ExtraButton7:'unknown',
Qt.MouseButton.ExtraButton8:'unknown',
Qt.MouseButton.ExtraButton9:'unknown',
Qt.MouseButton.ExtraButton10:'unknown',
Qt.MouseButton.ExtraButton11:'unknown',
Qt.MouseButton.ExtraButton12:'unknown',
Qt.MouseButton.ExtraButton13:'unknown',
Qt.MouseButton.ExtraButton14:'unknown',
Qt.MouseButton.ExtraButton15:'unknown',
Qt.MouseButton.ExtraButton16:'unknown',
Qt.MouseButton.ExtraButton17:'unknown',
Qt.MouseButton.ExtraButton18:'unknown',
Qt.MouseButton.ExtraButton19:'unknown',
Qt.MouseButton.ExtraButton20:'unknown',
Qt.MouseButton.ExtraButton21:'unknown',
Qt.MouseButton.ExtraButton22:'unknown',
Qt.MouseButton.ExtraButton23:'unknown',
Qt.MouseButton.ExtraButton24:'unknown',
}
