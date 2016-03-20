from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)    # Only one instance 
dialog = QDialog()              # window
dialog.show()                   # Show window
app.exec_()                     # exec_because reserved word in python

print("Testing push in branch")
