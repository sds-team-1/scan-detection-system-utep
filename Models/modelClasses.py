class Workspace:
    def __init__(self, name: str = '', projects: list = []):
        self.name:str = name
        self.projects:list = projects

    def get_mongo_encoded_workspace(self):
        return {
            'name': self.name,
            'projects': [project.get_mongo_encoded_project() for project in self.projects]
        }

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

class Scenario:
    def __init__(self, name : str, devices : list=[], networks : list=[]):
        self.name:str = name
        self.networks:list = networks
        self.devices:list = devices
    def get_mongo_encoded_scenario(self):
        return {
            'name': self.name,
            'devices': [device.get_mongo_encoded_node() for device in self.devices],
            'networks': [network.get_mongo_encoded_node() for network in self.networks]
        }


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
    listening: bool, 
    port: int, 
    ):
        # CORE Attributes
        self.id = id
        self.name = name
        self.type = type
        self.mac = mac
        self.ip = ip
        self.ip4_mask = "24"

        # Generic fields
        self.listening = listening
        self.port = port

    def get_mongo_encoded_node(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'mac': self.mac,
            'ip': self.ip,
            'ip4_mask': self.ip4_mask,
            'listening': self.listening,
            'port': self.port
        }

class ScannerNode(Node):
    def __init__(self, id: int, listening: bool, node_type: str, name: str, IP: str, \
                 port: int, MAC: str, network: int, us_pas, scanner_binary, arguments, \
                 iterations, max_parallel_runs, end_condition):
        super().__init__(id, listening, node_type, name, IP, port, MAC, network)
        self.us_pas = us_pas
        self.scanner_binary = scanner_binary
        self.arguments = arguments
        self.iterations = iterations
        self.max_parallel_runs = max_parallel_runs
        self.end_condition = end_condition