class Workspace:
    def __init__(self, name: str = '', projects: list = []):
        self._id:str = name
        self.name:str = name
        self.projects:list = projects

    def get_mongo_encoded_workspace(self):
        '''
        Returns a dictionary that
        can be understood by mongoDB
        '''
        return {
            '_id': self._id,
            'name': self.name,
            'projects': [project.get_mongo_encoded_project() for project in self.projects]
        }
    
    @staticmethod
    def create_workspace_from_mongo_encoded_workspace(mongo_encoded_workspace):
        '''
        Returns a Workspace object from a mongo_encoded_workspace (dictionary)
        '''
        return Workspace(
            name=mongo_encoded_workspace['name'],
            projects=[Project.create_project_from_mongo_encoded_project(mongo_encoded_project) for mongo_encoded_project in mongo_encoded_workspace['projects']]
        )


# The methods for the classes below have the same logic as the ones in the Workspace class

class Project:
    def __init__(self, name: str, max_units: int, scenarios: list = []):
        self.name:str = name
        self.max_units:int = max_units
        self.scenarios:list = scenarios

    def get_mongo_encoded_project(self):
        return {
            'name': self.name,
            'max_units': self.max_units,
            'scenarios': [scenario.get_mongo_encoded_scenario() for scenario in self.scenarios]
        }

    @staticmethod
    def create_project_from_mongo_encoded_project(mongo_encoded_project):
        return Project(
            name=mongo_encoded_project['name'],
            max_units=mongo_encoded_project['max_units'],
            scenarios=[Scenario.create_scenario_from_mongo_encoded_scenario(mongo_encoded_scenario) for mongo_encoded_scenario in mongo_encoded_project['scenarios']]
        )

class Scenario:
    def __init__(self, name : str, devices : list=[], networks : list=[]):
        self.name:str = name
        self.networks:list = networks
        self.devices:list = devices

        print("scenario created with name: " + self.name)
        print("scenario created withcount devices: " + str(len(self.devices)))
        print("scenario created withcount networks: " + str(len(self.networks)))
    def get_mongo_encoded_scenario(self):
        return {
            'name': self.name,
            'devices': [device.get_mongo_encoded_node() for device in self.devices],
            'networks': [network.get_mongo_encoded_node() for network in self.networks]
        }
    @staticmethod
    def create_scenario_from_mongo_encoded_scenario(mongo_encoded_scenario):
        return Scenario(
            name=mongo_encoded_scenario['name'],
            devices=[Node.create_node_from_mongo_encoded_node(mongo_encoded_node) for mongo_encoded_node in mongo_encoded_scenario['devices']],
            networks=[Node.create_node_from_mongo_encoded_node(mongo_encoded_node) for mongo_encoded_node in mongo_encoded_scenario['networks']]
        )


class Node: 
    '''
    Nodes that are used to define the networks
    and devices array in a scenario
    '''
    def __init__(
    self, 
    id: int, 
    name: str,
    type: str,
    mac: str, 
    ip: str,
    ip4_mask: str="24",
    core_listening: bool = True,
    vm_node_name: str = '',
    vm_node_username: str = '',
    vm_node_password: str = '',
    vm_binary_path: str = '',
    vm_args: str = ''
    ):
        # General Attributes
        self.id = id
        self.name = name
        self.type = type
        self.mac = mac
        self.ip = ip
        self.ip4_mask = ip4_mask

        # core fields
        self.core_listening = core_listening

        # vm fields
        self.vm_node_name = vm_node_name
        self.vm_node_username = vm_node_username
        self.vm_node_password = vm_node_password
        self.vm_binary_path = vm_binary_path
        self.vm_args = vm_args

    def get_mongo_encoded_node(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'mac': self.mac,
            'ip': self.ip,
            'ip4_mask': self.ip4_mask,
            'core_listening': self.core_listening,
            'vm_node_name': self.vm_node_name,
            'vm_node_username': self.vm_node_username,
            'vm_node_password': self.vm_node_password,
            'vm_binary_path': self.vm_binary_path,
            'vm_args': self.vm_args
        }
    
    @staticmethod
    def create_node_from_mongo_encoded_node(mongo_encoded_node):
        return Node(
            id=mongo_encoded_node['id'],
            name=mongo_encoded_node['name'],
            type=mongo_encoded_node['type'],
            mac=mongo_encoded_node['mac'],
            ip=mongo_encoded_node['ip'],
            ip4_mask=mongo_encoded_node['ip4_mask'],
            core_listening=mongo_encoded_node['core_listening'],
            vm_node_name=mongo_encoded_node['vm_node_name'],
            vm_node_username=mongo_encoded_node['vm_node_username'],
            vm_node_password=mongo_encoded_node['vm_node_password'],
            vm_binary_path=mongo_encoded_node['vm_binary_path'],
            vm_args=mongo_encoded_node['vm_args']
        )

    def get_copy_of_node(self):
        return Node(
            id=self.id,
            name=self.name,
            type=self.type,
            mac=self.mac,
            ip=self.ip,
            ip4_mask=self.ip4_mask,
            core_listening=self.core_listening,
            vm_node_name=self.vm_node_name,
            vm_node_username=self.vm_node_username,
            vm_node_password=self.vm_node_password,
            vm_binary_path=self.vm_binary_path,
            vm_args=self.vm_args
        )