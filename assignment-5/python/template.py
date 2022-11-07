from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 

# Get a reference to the main Maya application window
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 

class MyMayaWidget(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(MyMayaWidget, self).__init__(*args, **kwargs)
        
        # Parent widget under Maya main window        
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        # Set the UI display title and size    
        self.setWindowTitle('My Maya Widget')        
        self.setGeometry(50, 50, 250, 150)
        
        # Create a button with the text 'Test'
        # You can see all the available widgets available
        # in PySide here:
        # https://srinikom.github.io/pyside-docs/PySide/QtGui/index.html
        self.my_button = QPushButton('Test', self)

        # When the button is clicked, connect a signal to run
        # the function below
        self.my_button.clicked.connect(self.button_onClicked)   
         
    def button_onClicked(self):
        # Add code to run when the button is clicked here.
        # maya.cmds...
        print("Clicked!")
        
my_widget = MyMayaWidget()     
my_widget.show()
