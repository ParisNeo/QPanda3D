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

# import PySide stuff
from PySide6.QtWidgets import *
import sys
from panda3d.core import VBase4

class PandaTest(Panda3DWorld):
    def __init__(self, width=1024, height=768):
        Panda3DWorld.__init__(self, width=width, height=height)
        self.cam.setPos(0, -58, 6)
        self.win.setClearColorActive(True)
        self.win.setClearColor(VBase4(0.5, 0, 0, 1))
        self.cam.node().getDisplayRegion(0).setSort(20)
        #Create a panda        
        self.panda= loader.loadModel("panda")
        self.panda.reparentTo(render)
        self.panda.setPos(0,0,0)
                  
        #accept few keys
        self.accept("arrow_left", self.left)
        self.accept("arrow_right", self.right)
        self.accept("arrow_up", self.up)
        self.accept("arrow_down", self.down)
    def left(self):
        le_key_evt.setText("Left")
        self.camera.setPos( self.camera.getX()+1, self.camera.getY(), self.camera.getZ() )
    def right(self):
        le_key_evt.setText("right")
        self.camera.setPos( self.camera.getX()-1, self.camera.getY(), self.camera.getZ() )
    def up(self):
        le_key_evt.setText("Up")
        self.camera.setPos( self.camera.getX(), self.camera.getY()+1, self.camera.getZ() )
    def down(self):
        le_key_evt.setText("Down")
        self.camera.setPos( self.camera.getX(), self.camera.getY()-1, self.camera.getZ() )
if __name__ == "__main__":    
    world = PandaTest() 
    app = QApplication(sys.argv)
    appw=QMainWindow()
    appw.setGeometry(50, 50, 1024, 768)
    # Here, we create the panda3D widget and specify that we want the widget to stretch
    # The keep_ratio parameter tells weather the painter should keep the ratio of the original
    # environment or it can devorm it. If ratio is kept, then the original will be cropped
    main_widget=QWidget()
    main_widget.setLayout(QVBoxLayout())

    # SPanda3D Widget
    pandaWidget = QPanda3DWidget(world)#, stretch=True, keep_ratio=False)
    # Buttons Widget
    btn_widget = QWidget()
    btn_widget.setMaximumHeight(50)
    btn_widget.setLayout(QHBoxLayout())
    # Add them to the window
    main_widget.layout().addWidget(pandaWidget)
    main_widget.layout().addWidget(btn_widget)
    # Now let's create some buttons
    le_key_evt=QLineEdit("")
    btn_widget.layout().addWidget(le_key_evt)

    appw.setCentralWidget(main_widget)
    appw.show()
    sys.exit(app.exec())
    