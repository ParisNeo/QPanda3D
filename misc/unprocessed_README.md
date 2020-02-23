
# QPanda3D
!define(cite_)([!1](https://github.com/!1))
A working Panda3D wrapper for PyQt5
The objective is to be able to put on the same screen, panda3D and pyQT widgets.

This package is still a work in progress.
What works :

- Creating a panda3D world inside a seemlessly QWidget object that can be placed alog with other QT stuff
- Full access to panda3D objects, lights ...
- Keyboard press and up are supported starting from v 0.5
What doesn't work yet:
- Mouse and timed keyboard interactions

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

Starting from V 0.4, the widget is automatically resized without making any stretching artefacts. Resizing policy parameters (introduced in V 0.2) have been removed since they are no more needed.
  
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

## Special thanks

I want to thank all the contributers to this little opensource project.
In chronological order :

- Thanks to !cite_(fraca7) for his commit (Change film size according to widget resize)
- Many thanks to !cite_(nmevenkamp) for the valuable updates and bugfixes he apported to this project.

If other people want to contribute to this project, the're welcome.
