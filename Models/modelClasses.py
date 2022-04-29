class Workspace:
    def __init__(self, name: str = '', projects: list = []):
        self.name = name
        self.projects = projects


class Project:
    def __init__(self, name: str, max_units: int, scenarios: list = []):
        self.name = name
        self.max_units = max_units
        self.scenarios = scenarios


class Scenario:
    def __init__(self, name : str, links : list, nodes : list):
        self.name = name
        # self.networks = networks
        # self.devices = devices
        # self.links = links
        self.nodes = nodes
        self.links = links


class Node:
    def __init__(self, id: int, listening: bool, node_type: str, name: str,
                 IP: str, port: int, MAC: str, network: int):
        self.id = id
        self.listening = listening
        self.type = node_type
        self.name = name
        self.IP = IP
        self.port = port
        self.MAC = MAC
        self.network = network


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