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
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Panda imports
from panda3d.core import Texture, WindowProperties, CallbackGraphicsWindow
from panda3d.core import loadPrcFileData

from QPanda3D.QPanda3D_Buttons_Translation import QPanda3D_Button_translation
from QPanda3D.QPanda3D_Keys_Translation import QPanda3D_Key_translation
from QPanda3D.QPanda3D_Modifiers_Translation import QPanda3D_Modifier_translation
import builtins

__all__ = ["QPanda3DWidget"]


class QPanda3DSynchronizer(QTimer):
    def __init__(self, qPanda3DWidget, FPS=60):
        QTimer.__init__(self)
        self.qPanda3DWidget = qPanda3DWidget
        dt = 1000 // FPS
        self.setInterval(int(round(dt)))
        self.timeout.connect(self.tick)

    def tick(self):
        if self.isActive():
            try:
                builtins.base.taskMgr.step()
            except:
                pass
            self.qPanda3DWidget.update()

    def __del__(self):
        self.stop()



def get_panda_key_modifiers(evt):
    panda_mods = []
    qt_mods = evt.modifiers()
    for qt_mod, panda_mod in QPanda3D_Modifier_translation.items():
        if (qt_mods & qt_mod) == qt_mod:
            panda_mods.append(panda_mod)
    return panda_mods


def get_panda_key_modifiers_prefix(evt):
        # join all modifiers (except NoModifier, which is None) with '-'
    mods = [mod for mod in get_panda_key_modifiers(evt) if mod is not None]
    prefix = "-".join(mods)

    # Fix the case where the modifier key is pressed
    # alone without other things
    # if not things like control-control would be possible
    if isinstance(evt, QtGui.QMouseEvent):
        key = QPanda3D_Button_translation[evt.button()]
    elif isinstance(evt, QtGui.QKeyEvent):
        key = QPanda3D_Key_translation[evt.key()]
    elif isinstance(evt, QtGui.QWheelEvent):
        key = "wheel"
    else:
        raise NotImplementedError("Unknown event type")

    if key in mods:
        mods.remove(key)
        prefix = "-".join(mods)

    # if the prefix is not empty, append a '-'
    if prefix == "-":
        prefix = ""
    if prefix:
        prefix += "-"

    return prefix

class QPanda3DWidget(QWidget):
    """
    An interactive panda3D QWidget
    Parent : Parent QT Widget
    FPS : Number of frames per socond to refresh the screen
    debug: Switch printing key events to console on/off
    """

    def __init__(self, panda3DWorld, parent=None, FPS=60, debug=False):
        QWidget.__init__(self, parent)

        # set fixed geometry
        self.panda3DWorld = panda3DWorld
        self.panda3DWorld.set_parent(self)
        # Setup a timer in Qt that runs taskMgr.step() to simulate Panda's own main loop
        # pandaTimer = QTimer(self)
        # pandaTimer.timeout.connect()
        # pandaTimer.start(0)

        self.setFocusPolicy(Qt.StrongFocus)

        # Setup another timer that redraws this widget in a specific FPS
        # redrawTimer = QTimer(self)
        # redrawTimer.timeout.connect(self.update)
        # redrawTimer.start(1000/FPS)

        self.paintSurface = QPainter()
        self.rotate = QTransform()
        self.rotate.rotate(180)
        self.out_image = QImage()

        size = self.panda3DWorld.cam.node().get_lens().get_film_size()
        self.initial_film_size = QSizeF(size.x, size.y)
        self.initial_size = self.size()

        self.synchronizer = QPanda3DSynchronizer(self, FPS)
        self.synchronizer.start()

        self.debug = debug

    def mousePressEvent(self, evt):
        button = evt.button()
        try:
            b = f"{get_panda_key_modifiers_prefix(evt)}{QPanda3D_Button_translation[button]}"
            if self.debug:
                print(b)
            messenger.send(b,[{"x":evt.x(),"y":evt.y()}])
        except Exception as e:
            print("Unimplemented button. Please send an issue on github to fix this problem")
            print(e)

    def mouseMoveEvent(self, evt:QtGui.QMouseEvent):
        button = evt.button()
        try:
            b = "mouse-move"
            if self.debug:
                print(b)
            messenger.send(b,[{"x":evt.x(),"y":evt.y()}])
        except Exception as e:
            print("Unimplemented button. Please send an issue on github to fix this problem")
            print(e)

    def mouseReleaseEvent(self, evt):
        button = evt.button()
        try:
            b = f"{get_panda_key_modifiers_prefix(evt)}{QPanda3D_Button_translation[button]}-up"
            if self.debug:
                print(b)
            messenger.send(b,[{"x":evt.x(),"y":evt.y()}])
        except Exception as e:
            print("Unimplemented button. Please send an issue on github to fix this problem")
            print(e)

    def wheelEvent(self, evt):
        delta = evt.angleDelta().y()
        try:
            w = f"{get_panda_key_modifiers_prefix(evt)}wheel"
            if self.debug:
                print(f"{w} {delta}")
            messenger.send(w, [{"delta": delta}])
        except Exception as e:
            print("Unimplemented button. Please send an issue on github to fix this problem")
            print(e)

    def keyPressEvent(self, evt):
        key = evt.key()
        try:
            k = f"{get_panda_key_modifiers_prefix(evt)}{QPanda3D_Key_translation[key]}"
            if self.debug:
                print(k)
            messenger.send(k)
        except Exception as e:
            print("Unimplemented key. Please send an issue on github to fix this problem")
            print(e)

    def keyReleaseEvent(self, evt):
        key = evt.key()
        try:
            k = f"{get_panda_key_modifiers_prefix(evt)}{QPanda3D_Key_translation[key]}-up"
            if self.debug:
                print(k)
            messenger.send(k)
        except Exception as e:
            print("Unimplemented key. Please send an issue on github to fix this problem")
            print(e)

    def resizeEvent(self, evt):
        lens = self.panda3DWorld.cam.node().get_lens()
        lens.set_film_size(
            self.initial_film_size.width() * evt.size().width()
            / self.initial_size.width(),
            self.initial_film_size.height() * evt.size().height()
            / self.initial_size.height()
        )
        self.panda3DWorld.buff.setSize(evt.size().width(), evt.size().height())

    def minimumSizeHint(self):
        return QSize(400, 300)

    # Use the paint event to pull the contents of the panda texture to the widget
    def paintEvent(self, event):
        if self.panda3DWorld.screenTexture.mightHaveRamImage():
            self.panda3DWorld.screenTexture.setFormat(Texture.FRgba32)
            data = self.panda3DWorld.screenTexture.getRamImage().getData()
            img = QImage(data, self.panda3DWorld.screenTexture.getXSize(), self.panda3DWorld.screenTexture.getYSize(),
                         QImage.Format_ARGB32).mirrored()
            self.paintSurface.begin(self)
            self.paintSurface.drawImage(0, 0, img)

            self.paintSurface.end()

    def movePointer(self, device, x, y):
        # device: #FIXME not used yet, just to keep in same style of
        #   arguments for `showbase.win.movePointer(device,x,y)`
        # here x and y are the position you want to move mouse to;
        # note that x and y are not in the same scale of Qt window coordinate,
        # but expected to follow the same convention with the position given
        # by QMouseWatcherNode;

        widget_pos = self.mapToGlobal(QPoint(0, 0)) # get widget postion
        # scale and shift it back to qt coordinate, you can see the inverse
        # transformation of this in QMouseWatcherNode.getMouse()
        scaled_x = -1 + 2 * x / self.parent.width()
        scaled_y = -1 + 2 * y / self.parent.height()
        scaled_y = - scaled_y
        global_x = widget_pos.x() + int(scaled_x)
        global_y = widget_pos.y() + int(scaled_y)
        QCursor.setPos(global_x, global_y)
