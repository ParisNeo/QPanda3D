# -*- coding: utf-8-*-
"""
Module : QPanda3D_Translation_Modifiers
Author : Niklas Mevenkamp
Description :
    Contains a dictionary that translates QT keyboard events to panda3d
    keyboard events.
"""
# PyQt imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
__all__ = ["QPanda3D_Modifiers_Translation"]

QPanda3D_Modifier_translation ={
Qt.NoModifier:None,
Qt.ShiftModifier:'shift',
Qt.ControlModifier:'control',
Qt.AltModifier:'alt',
Qt.MetaModifier:'unknown',
Qt.KeypadModifier:'unknown',
Qt.GroupSwitchModifier:'unknown',
}