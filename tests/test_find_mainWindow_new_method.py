# madoodia@gmail.com
# this method of finding main window of host
# tested in maya and nuke, works fine
# in houdini and realflow does not support pyside
# but with pyqt4 it works fine

from PySide.QtGui import *


class PyblishGUI(QDialog):
    def __init__(self, parent=None):
        super(PyblishGUI, self).__init__(parent)

        self.textBox = QLineEdit()
        self.btn = QPushButton("Apply")
        layout = QVBoxLayout(self)
        layout.addWidget(self.textBox)
        layout.addWidget(self.btn)

        self.btn.clicked.connect(self.callMe)

        self.textBox.textEdited.connect(self.updateUi)
        self.updateUi()

    def callMe(self):
        print self.textBox.text()

    def updateUi(self):
        enable = not (self.textBox.text() == "")
        self.btn.setEnabled(enable)


# there is some problem with this method that should be solved
def getMainWindow():
    mainWindow = QApplication.activeWindow()
    while True:
        if mainWindow.parent():
            mainWindow = mainWindow.parent()
        else:
            break
    return mainWindow

win = PyblishGUI(parent=getMainWindow())
win.show()
