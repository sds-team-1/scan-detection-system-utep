import sys
from PyQt5 import QtWidgets

from views.captureManagerWindow import Ui_CaptureManagerWindow


app = QtWidgets.QApplication(sys.argv)



captureManager_Window = QtWidgets.QMainWindow()
captureManagerWindowUI = Ui_CaptureManagerWindow()
captureManagerWindowUI.setupCaptureManager(captureManager_Window)
captureManager_Window.setWindowTitle('Scan Detection System')
captureManager_Window.show()


sys.exit(app.exec_())
