from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # super(HelloWorld, self).__init__()                    # overwrite constructor
        # Container
        layout = QVBoxLayout()

        # Objects(widgets) within the container
        self.label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        # Modify object properties
        layout.addWidget(self.label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)
        
        button.clicked.connect(self.close)                      # Close app with close button
        line_edit.textChanged.connect(self.change_text_label)     # call handler to change label
        
    def change_text_label(self, text):
        self.label.setText(text)
        
# -------------------------- MAIN # ---------------------------------
# This code calls the main program
app = QApplication(sys.argv)                                    # Only one instance
dialog = HelloWorld()                                           # Window
dialog.show()                                                   # Show window
app.exec_()                                                     # exec_, because reserved word in python
