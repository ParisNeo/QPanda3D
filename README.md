
# QPanda3D

A working Panda3D wrapper for PySide6
The objective is to be able to put on the same screen, panda3D and QT widgets.

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
    
    sys.exit(app.exec())

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
    
    sys.exit(app.exec())

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

## Mouse events handling
Mouse position is sent from Qt interface to panda using messages. You can get these information using the following event handlers :
mouse1 :Mouse Button 1 Pressed
mouse2 :Mouse Button 2 Pressed
mouse3 :Mouse Button 3 Pressed
mouse1-up :Mouse Button 1 Released
mouse2-up :Mouse Button 2 Released
mouse3-up :Mouse Button 3 Released
wheel_up :Mouse Wheel rolled upwards
wheel_down :Mouse Wheel rolled downwards

When you handle those events, starting from version 0.2.9, you can add an event argument to your event handler method to receive relevent information about the actual position of the mouse in the Qt 2D canvas.

here is an example of how you can use this. You can also find a complete example in the examples list

```python
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
```
## Special thanks

I want to thank all the contributers to this little opensource project.
In chronological order :

- Thanks to [fraca7](https://github.com/fraca7) for his commit (Change film size according to widget resize)
- Many thanks to [nmevenkamp](https://github.com/nmevenkamp) for the valuable updates and bugfixes he apported to this project.
- Also thanks to [augasur](https://github.com/augasur) for bringing to our knowledge problems he faced while using pyinstaller with qpanda3d (preblem solved).
- Also thanks to [arthurpdesimone](https://github.com/arthurpdesimone) for bringing to our knowledge problems he faced while using mouse interaction.

If other people want to contribute to this project, the're welcome.
