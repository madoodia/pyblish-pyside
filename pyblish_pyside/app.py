# --------------------------------------------------- #
# Pyblish GUI with PySide
# madoodia@gmail.com
# pyblish.com
# for using we will import the app file and call show()
# --------------------------------------------------- #
from PySide import QtGui


class PyblishGUI(QtGui.QDialog):

    """The main Window of Pyblish GUI"""

    def __init__(self, parent=None):
        super(PyblishGUI, self).__init__(parent)

        self.resize(400, 400)
        self.setWindowTitle("Pyblish")


# # getting main window of host as parent of pyblish window
# def getMainWindow():
#     mainWindow = QtGui.QApplication.activeWindow()
#     while True:
#         if mainWindow.parent():
#             mainWindow = mainWindow.parent()
#         else:
#             break
#     return mainWindow

def show():
    # getting main window of host as parent of pyblish window
    # in this version we have non-singleton gui
    # for singleton version we should destroy the last window
    mainApp = QtGui.QApplication.activeWindow()
    # if win:
    #     win.destroy(True)
    win = PyblishGUI(parent=mainApp)
    win.show()
