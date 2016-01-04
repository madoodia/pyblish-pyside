# --------------------------------------------------- #
# Pyblish GUI with PySide
# madoodia@gmail.com
# pyblish.com
# the GUI is not Singleton
# for using we will import the app file and call show()
# for using:
#   import sys
#   sys.path.append(r'E:\Madoodia\_GitHub\pyblish-pyside\pyblish_pyside')
#   import app
#   app.show()
# --------------------------------------------------- #
from PySide import QtGui


class PyblishGUI(QtGui.QDialog):

    """The main Window of Pyblish GUI [is not Singleton]"""

    singleton = None

    def __init__(self, parent=None):
        super(PyblishGUI, self).__init__(parent)

        self.resize(400, 400)
        self.setWindowTitle("Pyblish")

    def closeEvent(self, event):
        self.close()


def getMainWindow():
    mainWindow = QtGui.QApplication.activeWindow()
    while True:
        lastWin = mainWindow.parent()
        if lastWin:
            mainWindow = lastWin
        else:
            break
    return mainWindow


def show():
    if PyblishGUI.singleton is not None:
        PyblishGUI.singleton.pos()
        PyblishGUI.singleton.show()
    else:
        win = PyblishGUI(parent=getMainWindow())
        PyblishGUI.singleton = win
        win.show()
