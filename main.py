import sys
from PyQt5 import QtWidgets
import json
import Database.DatabaseHelper
from views.databaseConfigWindow import Ui_databaseConfig_window

# dbHelper : Database.DatabaseHelper.SDSDatabaseHelper = Database.DatabaseHelper.SDSDatabaseHelper()

app = QtWidgets.QApplication(sys.argv)

databaseConfig_Window = QtWidgets.QDialog()
databaseConfigWindowUI = Ui_databaseConfig_window()
databaseConfigWindowUI.setupDatabaseConfig(databaseConfig_Window)

# Use the deaults to autofill the input boxes

databaseConfig_Window.show()

sys.exit(app.exec_())
