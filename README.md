# QPanda3D
A working Panda3D wrapper for PyQt5

The objective is to be able to put on the same screen, panda3D and pyQT widgets.

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
        base.cam.setPos(0, -28, 6)
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

## TODO
- Add widget resizing capacilities
- Add mouse and keyboard interactions
