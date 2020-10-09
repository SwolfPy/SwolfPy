# -*- coding: utf-8 -*-
"""
@author: msardar2

Solid Waste Optimization Life-cycle Framework in Python(SwolfPy)
"""


__all__ = [
    'Technosphere',
    'Project',
    'import_methods',
    'Optimization',
    'Monte_Carlo',
    'MyQtApp',
    'swolfpy'
]

__version__ = '0.1.9'


from .Technosphere import Technosphere
from .Project import Project
from .swolfpy_method import import_methods
from .Optimization import Optimization
from .Monte_Carlo import Monte_Carlo


from .UI.PySWOLF_run import MyQtApp
from PySide2 import QtCore, QtGui, QtWidgets

    
        
        
        
import sys

class swolfpy():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.qt_app  = MyQtApp()
        availableGeometry = self.app.desktop().availableGeometry(self.qt_app)
        self.qt_app.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2.85 / 3)
        self.qt_app.show()
        self.app.exec_()
        


