from Controllers.SDSController import SDSController
from dubs.DubAnalysisManager import DubAnalysisManager
from dubs.DubCaptureController import DubCaptureController
from dubs.DubDatabaseHelper import DubDatabaseHelper

sds_controller: SDSController = SDSController()
sds_controller.add_analysis_manager(DubAnalysisManager())
sds_controller.add_capture_manager(DubCaptureController())
sds_controller.add_mongo_connection(DubDatabaseHelper())

"""The purpose of this is to run in interactive mode. Run this as
    python3 -i inter_test_sdscontroller.py
    
    It will run with a prompt"""
print('sds_controller ready to test with all dubs')
