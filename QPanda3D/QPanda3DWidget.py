# -*- coding: utf-8-*-
"""
Module : QPanda3DWidget
Author : Saifeddine ALOUI
Description :
    This is the QWidget to be inserted in your standard PyQt5 application.
    It takes a Panda3DWorld object at init time.
    You should first create the Panda3DWorkd object before creating this widget.
"""
# PyQt imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtOpenGL
import OpenGL
OpenGL.ERROR_CHECKING = True
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL import error
import sys
# Panda imports
from panda3d.core import Texture, WindowProperties, CallbackGraphicsWindow
from panda3d.core import loadPrcFileData

__all__ = ["QPanda3DWidget"]

class QPanda3DWidget(QWidget):
    """
    An interactive panda3D QWidget
    Parent : Parent QT Widget
    w_geometry : default Widget geometry (only if not in a layout)
    stretch : Whether to stretch the scene to fit the widget layout
    FPS : Number of frames per socond to refresh the screen
    """    
    def __init__(self, panda3DWorld,  parent=None, w_geometry = (0, 0, 800, 600), stretch=False, keep_ratio=False, FPS=60):
        QtOpenGL.QGLWidget.__init__(self,  parent)
        gsg = None
        #set fixed geometry        
        self.setGeometry(w_geometry[0], w_geometry[1], w_geometry[2], w_geometry[3])
        self.panda3DWorld = panda3DWorld
        # Setup a timer in Qt that runs taskMgr.step() to simulate Panda's own main loop
        pandaTimer = QTimer(self)
        pandaTimer.timeout.connect(taskMgr.step)
        pandaTimer.start(0)
        self.setFocusPolicy(Qt.StrongFocus)



        # Setup another timer that redraws this widget in a specific FPS
        redrawTimer = QTimer(self)
        redrawTimer.timeout.connect(self.update)
        redrawTimer.start(1000/FPS)
        
        self.paintSurface = QPainter()
        self.rotate = QTransform()
        self.rotate.rotate(180)
        self.out_image = QImage()

        self.stretch = stretch
        self.keep_ratio = keep_ratio
    def keyPressEvent(self, evt):
        key=evt.key()
        if(key >= Qt.Key_Space and key <= Qt.Key_AsciiTilde):
            evt_val = "{}".format(chr(evt.key())).lower()
            print(evt_val)
            messenger.send(evt_val)
        else:
            print("Not ASCII")

    def resizeEvent(self, evt):
        pass
        """
        wp = WindowProperties()
        wp.setSize(self.width(), self.height())
        wp.setOrigin(self.x(),self.y())
        self.panda3DWorld.win.requestProperties(wp)
        """

    def minimumSizeHint(self):
        return QSize(400,300)

    def setStretch(self, stretch=False):
        """
        changes stretch  status
        """
        self.stretch = stretch

    def setKeep_raqtio(self, keep_ratio=False):
        """
        changes stretch  status
        """
        self.keep_ratio = keep_ratio
    
    # Use the paint event to pull the contents of the panda texture to the widget
    def paintEvent(self,  event):
        if self.panda3DWorld.screenTexture.mightHaveRamImage():
            self.panda3DWorld.screenTexture.setFormat(Texture.FRgba32)
            data = self.panda3DWorld.screenTexture.getRamImage().getData()
            img = QImage(data, self.panda3DWorld.screenTexture.getXSize(), self.panda3DWorld.screenTexture.getYSize(), QImage.Format_ARGB32).mirrored()
            self.paintSurface.begin(self)
            if(self.stretch):
                target = QRectF(0, 0, self.width(),self.height())
                if(self.keep_ratio):
                    if(self.width()<self.height()):
                        h= self.panda3DWorld.screenTexture.getYSize()
                        res=float(self.width())/float(self.height())
                        w= res*h
                        src = QRectF(0, 0, w, h)
                    else:
                        w=  self.panda3DWorld.screenTexture.getXSize()                        
                        res=float(self.height())/float(self.width())
                        h=  res*w
                        src = QRectF(0, 0, w, h)
                else:
                    src = QRectF(0, 0, self.panda3DWorld.screenTexture.getXSize(), self.panda3DWorld.screenTexture.getYSize())
                self.paintSurface.drawImage(target, img, src)
            else:
                self.paintSurface.drawImage(0,0, img)

            self.paintSurface.end()
    