import os
from datetime import datetime

class Scenario:
    def __init__(self, name:str, parent_path:str, create_time = datetime.now().timestamp()):
        self.name = name
        self.size = 0  #number of nodes
        self.node = []
        self.path = os.path.join(parent_path,self.name)
        self.create_folder()

    def new_scenario(self, new:Scenario) -> list:
        self.scenario.append(new)
        self.size = os.path.getsize(self.path)
        return self.scenario

    def remove_scenario(self,old:Scenario)->list:
        self.scenario

