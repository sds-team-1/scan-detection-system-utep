import sys
from PyQt5 import QtWidgets
import json
import Database.DatabaseHelper
from views.databaseConfigWindow import Ui_databaseConfig_window

# App starts with the database config window
app = QtWidgets.QApplication(sys.argv)

databaseConfig_Window = QtWidgets.QDialog()
databaseConfigWindowUI = Ui_databaseConfig_window()
databaseConfigWindowUI.setupDatabaseConfig(databaseConfig_Window)


databaseConfig_Window.show()

sys.exit(app.exec_())
