# QPanda3D
A working Panda3D wrapper for PyQt5
The objective is to be able to put on the same screen, panda3D and pyQT widgets.

This package is still a work in progress.
What works :
- Creating a panda3D world inside a seemlessly QWidget object that can be placed alog with other QT stuff
- Full access to panda3D objects, lights ...

What doesn't work yet:
- Mouse and keyboard interactions
- QWidget resizing. For now, the widget size is fixed, which means that you can not use it alongside with other Qt widgets without cropping the 3D scene.

## Installation
```bash
pip install QPanda3D
```
## Usage
1 - create your world by inheriting from Panda3DWorld
```python
from QPanda3D.Panda3DWorld import Panda3DWorld
class MyWorld(Panda3DWorld):
        Panda3DWorld.__init__(self)
        # from this point, act as if you are defining a classic panda3D environment
        self.cam.setPos(0, -28, 6)
        self.testModel = loader.loadModel('panda')
        self.testModel.reparentTo(render)
```
2 - In your main, just create an instance of your world, create a Q
```python
from QPanda3D.QPanda3DWidget import QPanda3DWidget
if __name__ == "__main__":    
    world = MyWorld() 
    
    app = QApplication(sys.argv)
    appw=QMainWindow()
    appw.setGeometry(50, 50, 800, 600)

    pandaWidget = QPanda3DWidget(world)
    appw.setCentralWidget(pandaWidget)
    appw.show()
    
    sys.exit(app.exec_())    

```

## Widget resizing policy
Starting from V 0.2, it is possible to change your QWidget size at runtime.
You just need to specify the resizing policies when creating the QPanda3D widgt.

Two new parameters can  be used:
- stretch : a boolean to specify if the graphical zone should stratch when the widget is resized or not
- keep_ratio : tells the widget to keep the ratio of the screen which can be interesting if you don't want the view to be deformed if the stretching changes the ratio too much.

from QPanda3D.QPanda3DWidget import QPanda3DWidget
if __name__ == "__main__":    
    world = MyWorld() 
    
    app = QApplication(sys.argv)
    appw=QMainWindow()
    appw.setGeometry(50, 50, 800, 600)

    pandaWidget = QPanda3DWidget(world, stretch=True, keep_ratio=True)
    appw.setCentralWidget(pandaWidget)
    appw.show()
    
    sys.exit(app.exec_())    

```

you can also tell the Panda3DWorld object what is the default view size that you prefer when creating it.

```python
from QPanda3D.Panda3DWorld import Panda3DWorld
class MyWorld(Panda3DWorld):
        Panda3DWorld.__init__(self, width=1024, height=768)
        # from this point, act as if you are defining a classic panda3D environment
        self.cam.setPos(0, -28, 6)
        self.testModel = loader.loadModel('panda')
        self.testModel.reparentTo(render)
```
Just make sure that your ratio is adequate with your real widget size.

## TODO
- Add mouse and keyboard interactions
