# -*- coding: utf-8-*-
"""
Module : Panda3DWorld
Author : Saifeddine ALOUI
Description :
    Inherit this object to create your custom world
"""

# PyQt imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Panda imports
from panda3d.core import loadPrcFileData
#loadPrcFileData("", "window-type none") # Set Panda to draw its main window in an offscreen buffer
from direct.showbase.DirectObject import DirectObject
from panda3d.core import GraphicsOutput,  Texture, ConfigVariableManager

# Set up Panda environment
from direct.showbase.ShowBase import ShowBase

__all__ = ["Panda3DWorld"]

class Panda3DWorld(ShowBase):  
    """
    Panda3DWorld : A class to handle all panda3D world manipulation
    """

    def __init__(self, width=800, height=600, is_fullscreen=False):
        cvMgr = ConfigVariableManager.getGlobalPtr()
        cvMgr.listVariables()
        loadPrcFileData("","win-size {} {}".format(width, height))
        if(is_fullscreen):
            loadPrcFileData("","fullscreen #t")
        else:
            loadPrcFileData("", "window-type offscreen") # Set Panda to draw its main window in an offscreen buffer
        ShowBase.__init__(self)
        self.disableMouse()
        self.screenTexture = Texture()
        self.screenTexture.setMinfilter(Texture.FTLinear)
        self.screenTexture.setFormat(Texture.FRgba32)
        self.win.addRenderTexture(self.screenTexture, GraphicsOutput.RTMCopyRam)

