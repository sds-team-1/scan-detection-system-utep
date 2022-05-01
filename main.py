import sys
from PyQt5 import QtWidgets
from views.chooseWorkspace import Ui_workspace_window
import json
import Database.DatabaseHelper
from views.databaseConfigWindow import Ui_databaseConfig_window

# dbHelper : Database.DatabaseHelper.SDSDatabaseHelper = Database.DatabaseHelper.SDSDatabaseHelper()

app = QtWidgets.QApplication(sys.argv)

databaseConfig_Window = QtWidgets.QDialog()
databaseConfigWindowUI = Ui_databaseConfig_window()
databaseConfigWindowUI.setupDatabaseConfig(databaseConfig_Window)

# Commenting out for now to prevent dependencies
# with open('conf/db_config.json') as mongo_ip_file:
#     database_ip_dict = json.load(mongo_ip_file)
#     ip = database_ip_dict['ip']
#     databaseConfigWindowUI.databaseConfigIPInput_databaseConfigWindow.setText(ip)
#     port = database_ip_dict['port']
#     databaseConfigWindowUI.databaseConfigPortInput_databaseConfigWindow.setText(port)


# Use the deaults to autofill the input boxes

databaseConfig_Window.show()

sys.exit(app.exec_())
