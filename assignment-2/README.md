# Assignment 2

Make a python script that does the following:
* Runs Maya in standalone mode
* Demonstrates one of the API commands found here: https://help.autodesk.com/cloudhelp/2022/ENU/Maya-Tech-Docs/Commands/index.html (examples: create geometry, add attributes, assign materials)
* Uses argparse to take some user input
* Saves the result Maya file (hint: look at `cmds.file` in the Command Reference)

Your `README.md` should include:
*  A description of what your script does
* The arguments it takes
* An example of how to run it

## Code Examples from class



Generating a cube in Maya standalone mode
```python
import maya.standalone
maya.standalone.initialize()

import maya.cmds

print("Creating a cube...")
maya.cmds.polyCube()
print(maya.cmds.ls(geometry=True))
```

Using `argparse` to take user input:
```python
import argparse

parser = argparse.ArgumentParser(description='This script creates a bunch of cubes.')
parser.add_argument('num_cubes', type=int, help="Number of cubes")

args = parser.parse_args()

import maya.standalone
maya.standalone.initialize()

import maya.cmds

print("Creating {} cube(s)...".format(args.num_cubes))

for i in range(args.num_cubes):
    print("Created cube #{}".format(i))
    maya.cmds.polyCube()

print("Meshes in the Maya scene:")
print(maya.cmds.ls(geometry=True))
```

Building a PySide widget in Maya
```python
from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 

class MyMayaWidget(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(MyMayaWidget, self).__init__(*args, **kwargs)
        
        #Parent widget under Maya main window        
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        #Set the object name     
        self.setWindowTitle('My Maya Widget')        
        self.setGeometry(50, 50, 250, 150)
        
        self.my_button = QPushButton('Test', self)
        self.my_button.clicked.connect(self.button_onClicked)   
         
    def button_onClicked(self):
        print("Clicked!")
        
my_widget = MyMayaWidget()     
my_widget.show()
```

Using a Qt Creator UI file
```python
from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from shiboken2 import wrapInstance 

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 

class MyMayaWidget(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(MyMayaWidget, self).__init__(*args, **kwargs)
        
        #Parent widget under Maya main window        
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        #Set the object name     
        self.setWindowTitle('My Maya Widget')        
        self.setGeometry(50, 50, 250, 150)
        
        self.initUI()  
         
    def initUI(self):        
        loader = QUiLoader()              
        file = QFile("./dialog.ui")        
        file.open(QFile.ReadOnly)        
        self.ui = loader.load(file, parentWidget=self)        
        file.close()
        
    def button_onClicked(self):
        print("Clicked!")
        
my_widget = MyMayaWidget()     
my_widget.show()

```