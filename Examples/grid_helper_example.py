# -*- coding: utf-8-*-
"""
Module : buttons_example
Author : Saifeddine ALOUI
Description :
    This is an example of how we can put togather a simple Panda3D Word 
    wrapped inside a QMainWindow and add QT pushbuttons that interact with the world.
    This uses the Env_Grid_Maker helper to make a 3D gridin the scene 
"""

from QPanda3D.Panda3DWorld import Panda3DWorld
from QPanda3D.QPanda3DWidget import QPanda3DWidget
from QPanda3D.Helpers.Env_Grid_Maker import *
# import PySide stuff
from PySide6.QtWidgets import *
import sys
from panda3d.core import AmbientLight, DirectionalLight, Point3, Vec4
from direct.interval.IntervalGlobal import Sequence, Parallel

class PandaTest(Panda3DWorld):
    def __init__(self, width=1024, height=768):
        Panda3DWorld.__init__(self, width=width, height=height)
        self.cam.setPos(0, -58, 30)
        self.cam.setHpr(0, -30, 0)
        self.win.setClearColorActive(True)
        self.win.setClearColor(VBase4(0, 0, 0, 1))
        self.cam.node().getDisplayRegion(0).setSort(20)
        #Create a panda        
        self.panda= loader.loadModel("panda")
        self.panda.reparentTo(render)
        self.panda.setPos(0,0,0)
        
        self.grid_maker=Env_Grid_Maker()
        self.grid=self.grid_maker.create()
        self.grid.reparentTo(render)
        self.grid.setLightOff() # THE GRID SHOULD N OT BE LIT

        # Now create some lights to apply to everything in the scene.
         
        # Create Ambient Light
        ambientLight = AmbientLight( 'ambientLight' )
        ambientLight.setColor( Vec4( 0.1, 0.1, 0.1, 1 ) )
        ambientLightNP = render.attachNewNode( ambientLight )
        render.setLight(ambientLightNP)
         
        # Directional light 01
        directionalLight = DirectionalLight( "directionalLight" )
        directionalLight.setColor( Vec4( 0.8, 0.1, 0.1, 1 ) )
        directionalLightNP = render.attachNewNode( directionalLight )
        # This light is facing backwards, towards the camera.
        directionalLightNP.setHpr(180, -20, 0)
        directionalLightNP.setPos(10,-100,10)
        render.setLight(directionalLightNP)
         
        # If we did not call setLightOff() first, the green light would add to
        # the total set of lights on this object.  Since we do call
        # setLightOff(), we are turning off all the other lights on this
        # object first, and then turning on only the green light.
        self.panda.setLightOff()
        self.jump_up = self.panda.posInterval(1.0, Point3(0, 0, 5), blendType="easeOut")
        self.jump_down = self.panda.posInterval(1.0, Point3(0, 0, 0), blendType="easeIn")
        self.jump_seq=Sequence(self.jump_up,self.jump_down)

        self.jump_up2 = self.panda.posInterval(1.0, Point3(10, 0, 15))
        self.jump_down2 = self.panda.posInterval(1.0, Point3(0, 0, 0))
        self.roll_left = self.panda.hprInterval(1.0, Point3(0, 0, 180))
        self.roll_right = self.panda.hprInterval(1.0, Point3(0, 0, 0))
        self.roll_seq=Sequence(Parallel(self.jump_up2,self.roll_left),Parallel(self.jump_down2,self.roll_right))

    def jump(self):
        self.jump_seq.start()

    def roll(self):
        self.roll_seq.start()

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
    btn_jump=QPushButton("Jump")
    btn_widget.layout().addWidget(btn_jump)
    btn_jump.clicked.connect(world.jump)

    btn_roll=QPushButton("Roll")
    btn_widget.layout().addWidget(btn_roll)
    btn_roll.clicked.connect(world.roll)

    appw.setCentralWidget(main_widget)
    appw.show()
    sys.exit(app.exec())
    