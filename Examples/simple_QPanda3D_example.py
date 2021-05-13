# -*- coding: utf-8-*-
"""
Module : simple_QPanda3D_example
Author : Saifeddine ALOUI
Description :
    This is an example of how we can put togather a simple Panda3D Word 
    wrapped inside a QMainWindow.
"""

from QPanda3D.Panda3DWorld import Panda3DWorld
from QPanda3D.QPanda3DWidget import QPanda3DWidget
# import PyQt5 stuff
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from panda3d.core import Point3, Vec3, Vec4, VBase4
from direct.interval.LerpInterval import LerpHprInterval
from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenImage import OnscreenImage

class PandaTest(Panda3DWorld):
    """
    This is the class that defines our world
    It inherits from Panda3DWorld that inherits from 
    Panda3D's ShowBase class
    """
    def __init__(self):
        Panda3DWorld.__init__(self)
        self.cam.setPos(0, -28, 6)
        self.win.setClearColorActive(True)
        self.win.setClearColor(VBase4(0, 0.5, 0, 1))        
        self.testModel = loader.loadModel('panda')
        self.testModel.reparentTo(render)

        # This rotates the actor 180 degrees on heading and 90 degrees on pitch.
        myInterval4 = self.testModel.hprInterval(1.0, Vec3(360, 0, 0))
        myInterval4.loop()

if __name__ == "__main__":    
    world = PandaTest() 
    
    app = QApplication(sys.argv)
    appw=QMainWindow()
    appw.setGeometry(50, 50, 800, 600)

    pandaWidget = QPanda3DWidget(world)
    appw.setCentralWidget(pandaWidget)
    appw.show()
    
    sys.exit(app.exec_())    
    