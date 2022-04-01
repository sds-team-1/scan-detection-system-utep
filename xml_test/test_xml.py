#! /usr/bin/env python3
import xmltodict
import os


class XmlHelper:
    config = '<links><link node1="1" node2="4">' \
            '<iface2 id="0" name="eth0" mac="00:00:00:aa:00:04" ip4="10.0.1.20" ip4_mask="24" ip6="2001:0:0:1::14" ip6_mask="64"/>' \
            '<options delay="0" bandwidth="0" loss="0.0" dup="0" jitter="0" unidirectional="0" buffer="0"/>' \
            '</link>' \
            '<link node1="1" node2="3">' \
            '<iface2 id="1" name="eth0" mac="00:00:00:aa:00:05" ip4="10.0.1.21" ip4_mask="24" ip6="2001:0:0:1::15" ip6_mask="64"/>' \
            '<options delay="0" bandwidth="0" loss="0.0" dup="0" jitter="0" unidirectional="0" buffer="0"/>' \
            '</link>' \
            '</links>' \
            '<session_origin lat="47.579166412353516" lon="-122.13232421875" alt="2.0" scale="150.0"/>' \
             '<session_options>' \
             '<configuration name="controlnet" value=""/>' \
             '<configuration name="controlnet0" value=""/>' \
             '<configuration name="controlnet1" value=""/>' \
             '<configuration name="controlnet2" value=""/>' \
             '<configuration name="controlnet3" value=""/>' \
             '<configuration name="controlnet_updown_script" value=""/>' \
             '<configuration name="enablerj45" value="1"/>' \
             '<configuration name="preservedir" value="0"/>' \
             '<configuration name="enablesdt" value="0"/>' \
             '<configuration name="sdturl" value="tcp://127.0.0.1:50000/"/>' \
             '<configuration name="ovs" value="0"/>' \
             '<configuration name="platform_id_start" value="1"/>' \
             '<configuration name="nem_id_start" value="1"/>' \
             '<configuration name="link_enabled" value="1"/>' \
             '<configuration name="loss_threshold" value="30"/>' \
             '<configuration name="link_interval" value="1"/>' \
             '<configuration name="link_timeout" value="4"/>' \
             '<configuration name="mtu" value="0"/>' \
             '</session_options>' \
             '<session_metadata>' \
             '<configuration name="edges" value="[]"/>' \
             '<configuration name="canvas" value="{&quot;gridlines&quot;: true, &quot;canvases&quot;: [{&quot;id&quot;: 1, &quot;wallpaper&quot;: null, &quot;wallpaper_style&quot;: 1, &quot;fit_image&quot;: false, &quot;dimensions&quot;: [1000, 750]}]}"/>' \
             '<configuration name="hidden" value="[]"/>' \
             '<configuration name="shapes" value="[]"/>' \
             '</session_metadata>' \
             '<default_services>' \
             '<node type="mdr">' \
             '<service name="zebra"/>' \
             '<service name="OSPFv3MDR"/>' \
             '<service name="IPForward"/>' \
             '</node>' \
             '<node type="PC">' \
             '<service name="DefaultRoute"/>' \
             '</node>' \
             '<node type="prouter"/>' \
             '<node type="router">' \
             '<service name="zebra"/>' \
             '<service name="OSPFv2"/>' \
             '<service name="OSPFv3"/>' \
             '<service name="IPForward"/>' \
             '</node>' \
             '<node type="host">' \
             '<service name="DefaultRoute"/>' \
             '<service name="SSH"/>' \
             '</node>' \
             '</default_services>' \
             '</scenario>'

    id_counter = 0
    formatted_dict = {}
    xml_str = ""
    networks_str = ""
    devices_str = ""

    def __init__(self, input_dict):
        self.input_dict = input_dict

    def replace_key_XML(self, new_str, old_str):
        self.xml_str = self.xml_str.replace(new_str, old_str)

    def create_xml_string(self):
        self.xml_str = xmltodict.unparse(self.formatted_dict, short_empty_elements=True)
        self.replace_key_XML(
            xmltodict.unparse(self.formatted_dict["scenario"]["networks"], short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', ""), self.networks_str)
        self.replace_key_XML(
            xmltodict.unparse(self.formatted_dict["scenario"]["devices"], short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', ""), self.devices_str)

        self.xml_str = self.xml_str[:len(self.xml_str)-11] + self.config

    def create_xml_file(self):
        xmlfile = open(f"{self.input_dict['scenario_name']}.xml", "w")
        xmlfile.write(self.xml_str)
        xmlfile.close()

    def format_dict(self):
        self.formatted_dict = {"scenario": {'@name': os.getcwd()}}
        networks = self.format_networks(self.input_dict['nodes'])
        self.formatted_dict["scenario"]["networks"] = networks["networks"]

        devices = self.format_devices(self.input_dict['nodes'])
        self.formatted_dict["scenario"]["devices"] = devices["devices"]

    def format_devices(self, nodes):
        devices_dict = {"devices": {}}

        for i in range(len(nodes)):
            self.id_counter += 1

            self.devices_str = self.devices_str + xmltodict.unparse(
                {'device': {'@id': str(self.id_counter), '@name': "n" + str(self.id_counter),
                            '@icon': "", "@canvas": "1", "@type": nodes[i]["type"],
                            "position": self.format_position()}}, short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', "")
            devices_dict["devices"].update(
                {'device': {'@id': str(self.id_counter), '@name': "n" + str(self.id_counter),
                            '@icon': "", "@canvas": "1", "@type": nodes[i]["type"],
                            "position": self.format_position()}})
        self.id_counter += 1
        self.devices_str = self.devices_str + xmltodict.unparse(
            {'device': {'@id': str(self.id_counter), '@name': "n" + str(self.id_counter),
                        '@icon': "", "@canvas": "1", "@type": "router",
                        "position": self.format_position()}}, short_empty_elements=True).replace(
            '<?xml version="1.0" encoding="utf-8"?>\n', "")
        devices_dict["devices"].update(
            {'device': {'@id': str(self.id_counter), '@name': "n" + str(self.id_counter),
                        '@icon': "", "@canvas": "1", "@type": "router",
                        "position": self.format_position()}})
        return devices_dict

    def format_networks(self, nodes):
        network_dict = {"networks": {}}
        subnets = self.find_subnets(nodes)
        switches = len(subnets)
        # router = {'network': {'@id': str(id_counter+1), '@name': "n" + str(id_counter), '@icon': "", "@canvas": "1", "@type": "SWITCH", "position": format_position()}}
        # network_dict["networks"] = router

        for i in range(switches):
            self.id_counter += 1
            self.networks_str = self.networks_str + xmltodict.unparse(
                {'network': {'@id': str(self.id_counter), '@name': "n" + str(self.id_counter),
                             '@icon': "", "@canvas": "1", "@type": "SWITCH",
                             "position": self.format_position()}}, short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', "")
            network_dict["networks"].update(
                {'network': {'@id': str(self.id_counter), '@name': "n" + str(self.id_counter),
                             '@icon': "", "@canvas": "1", "@type": "SWITCH",
                             "position": self.format_position()}})
        return network_dict

    def format_position(self):
        position = {'@x': "617.0", '@y': "609.0", '@lat': "47.57363051698441", "@lon": "-122.12401031079544", "@alt": "2.0"}
        return position

    def format_configservices(self):
        config = {}

    def find_subnets(self, nodes):
        subnets = {}
        for node in nodes:
            ip_split = node['ip'].split(".")
            subnet = ip_split[0] + "." + ip_split[1] + "." + ip_split[2] + ".n"
            if subnet in subnets:
                subnets[subnet] += 1
            else:
                subnets[subnet] = 1
        return subnets

    def get_xml_str(self):
        return self.xml_str

    def get_networks_str(self):
        return self.networks_str


input_dict_input = {
    "nodes": [
        {
            "id": 9,
            "listening": False,
            "type": "PC",
            "name": "n1",
            "ip": "10.0.0.1",
            "port": 8888,
            "MAC": "99:00:99:99:99:99",
            "network": 0
        },
        {
            "id": 9,
            "listening": False,
            "type": "PC",
            "name": "n1",
            "ip": "10.0.0.2",
            "port": 8888,
            "MAC": "99:00:99:99:99:98",
            "network": 0
        },
        {
            "id": 10,
            "type": "PC",
            "name": "n5",
            "ip": "10.0.1.1",
            "port": 8889,
            "MAC": "",
            "network": 1,
            "username/pass": "root/pass",
            "scanner_binary": "/usr/bin/nmap",
            "arguments": "--ts -v -ip 10.0.0.1",
            "iterations": 1,
            "parallel_runs": 1,
            "end_condition": ""
        }
    ],
    "scenario_name": "scenarioA",
    "project_name": "projectA",
    "workspace_name": "workspaceA"
}

xml = XmlHelper(input_dict_input)
xml.format_dict()
xml.create_xml_string()
xml.create_xml_file()
print(xml.get_xml_str())
