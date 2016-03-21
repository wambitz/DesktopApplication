from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # super(HelloWorld, self).__init__() # overwrite constructor
        # Container
        layout = QVBoxLayout()

        # Objects(widgets) within the container
        label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        # Modify object properties
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

# -------------------------- MAIN # ---------------------------------
# This code calls the main program
app = QApplication(sys.argv)    # Only one instance 
dialog = HelloWorld()              # window
dialog.show()                   # Show window
app.exec_()                     # exec_because reserved word in python

