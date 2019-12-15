# -*- coding: utf-8-*-
"""
Module : QMouseWatcherNode
Author : Niklas Mevenkamp
Description :
    This is a MouseWatcherNode implementation that accesses
    mouse position and button states through a parent QWidget.
"""

# PyQt imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Panda imports
from panda3d.core import *

__all__ = ["QMouseWatcherNode"]


class QMouseWatcherNode(MouseWatcher):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

    def getMouse(self, *args, **kwargs):
        # map global QCursor pixel position to parent Widget coordinates
        pos = self.parent.mapFromGlobal(QCursor.pos())

        # map absolute pixel positions to relative ones
        rel_x = -1 + 2 * pos.x() / self.parent.width()
        rel_y = -1 + 2 * pos.y() / self.parent.height()

        # invert y
        rel_y = -rel_y

        return LPoint2(rel_x, rel_y)

    def hasMouse(self):
        return isinstance(self.parent, QWidget)
