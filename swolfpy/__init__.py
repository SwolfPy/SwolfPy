# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:22:24 2020

@author: msardar2
"""


__all__ = [
    'Distance',
    'project',
    'import_methods',
    'ParallelData',
    'MyQtApp',
    'swolfpy'
]

__version__ = '0.1.5'

# module level doc-string
__doc__ = """
Solid Waste Optimization Life-cycle Framework in Python(SwolfPy)
"""


from .Distance import Distance
from .project_class import project
from .SWOLF_method import import_methods
from .building_matrices import ParallelData
from .UI.PySWOLF_run import MyQtApp
from PySide2 import QtCore, QtGui, QtWidgets

class swolfpy():
    def __init__(self):
        self.app = QtWidgets.QApplication()
        self.qt_app  = MyQtApp()
        self. qt_app.show()
        self.app.exec_()


