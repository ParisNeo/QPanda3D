# -*- coding: utf-8-*-
"""
Module : QPanda3D_Translation_Buttons
Author : Niklas Mevenkamp
Description :
    Contains a dictionary that translates QT mouse events to panda3d
    mouse events.
"""
# PyQt imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
__all__ = ["QPanda3D_Keys_Translation"]

QPanda3D_Button_translation ={
Qt.NoButton:'',
Qt.AllButtons:'unknown',
Qt.LeftButton:'mouse1',
Qt.RightButton:'mouse2',
Qt.MidButton:'mouse3',
Qt.MiddleButton:'mouse3',
Qt.BackButton:'unknown',
Qt.XButton1:'unknown',
Qt.ExtraButton1:'unknown',
Qt.ForwardButton:'unknown',
Qt.XButton2:'unknown',
Qt.ExtraButton2:'unknown',
Qt.TaskButton:'unknown',
Qt.ExtraButton3:'unknown',
Qt.ExtraButton4:'unknown',
Qt.ExtraButton5:'unknown',
Qt.ExtraButton6:'unknown',
Qt.ExtraButton7:'unknown',
Qt.ExtraButton8:'unknown',
Qt.ExtraButton9:'unknown',
Qt.ExtraButton10:'unknown',
Qt.ExtraButton11:'unknown',
Qt.ExtraButton12:'unknown',
Qt.ExtraButton13:'unknown',
Qt.ExtraButton14:'unknown',
Qt.ExtraButton15:'unknown',
Qt.ExtraButton16:'unknown',
Qt.ExtraButton17:'unknown',
Qt.ExtraButton18:'unknown',
Qt.ExtraButton19:'unknown',
Qt.ExtraButton20:'unknown',
Qt.ExtraButton21:'unknown',
Qt.ExtraButton22:'unknown',
Qt.ExtraButton23:'unknown',
Qt.ExtraButton24:'unknown',
}