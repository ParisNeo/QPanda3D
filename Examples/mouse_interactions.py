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
                  
        #accept few mouse events
        self.accept('mouse1', self.mousePressEventLeft)
        self.accept("mouse2", self.wheelEvent)
        self.accept("mouse1-up", self.mouseReleaseEventLeft)
        self.accept("mouse-move", self.mouseMoveEvent)

    def mousePressEventLeft(self, evt:dict):
        le_key_evt.setText(f"press @ {evt['x']},{evt['y']}")
    def mouseReleaseEventLeft(self, evt:dict):
        le_key_evt.setText(f"release @ {evt['x']},{evt['y']}")
    def wheelEvent(self, evt:dict):
        le_key_evt.setText(f"Wheel with {evt['delta']}")
    def mouseMoveEvent(self, evt:dict):
        le_key_evt.setText(f"Mouse moved to  {evt['x']},{evt['y']}")

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
    