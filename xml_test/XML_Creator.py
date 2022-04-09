#! /usr/bin/env python3
import xmltodict
import os


class XmlHelper:
    config = '<session_origin lat="47.579166412353516" lon="-122.13232421875" alt="2.0" scale="150.0"/>' \
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

    id_counter = 1
    formatted_dict = {}
    xml_str = ""
    networks_str = ""
    devices_str = ""
    links_str = ""

    def __init__(self, input_dict):
        self.input_dict = input_dict

    def replace_key_XML(self, new_str, old_str):
        self.xml_str = self.xml_str.replace(new_str, old_str)

    def create_xml_string(self):
        self.xml_str = xmltodict.unparse(self.formatted_dict, short_empty_elements=True)


        self.replace_key_XML(
            xmltodict.unparse(self.formatted_dict["scenario"]["networks"], short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', ""), self.networks_str)
        if len(self.input_dict["devices"]) > 0:
            self.replace_key_XML(
                xmltodict.unparse(self.formatted_dict["scenario"]["devices"], short_empty_elements=True).replace(
                    '<?xml version="1.0" encoding="utf-8"?>\n', ""), self.devices_str)
        
        self.replace_key_XML(
            xmltodict.unparse(self.formatted_dict["scenario"]["links"], short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', ""), self.links_str)

        self.xml_str = self.xml_str[:len(self.xml_str)-11] + self.config

    def create_xml_file(self):
        xmlfile = open(f"{self.input_dict['name']}.xml", "w")
        xmlfile.write(self.xml_str)
        xmlfile.close()

    def format_dict(self):
        self.formatted_dict = {"scenario": {'@name': os.getcwd() + f'\{self.input_dict["name"]}'}}

        networks = self.format_networks()
        self.formatted_dict["scenario"]["networks"] = networks["networks"]

        if len(self.input_dict["devices"]) > 0:
            devices = self.format_devices()
            self.formatted_dict["scenario"]["devices"] = devices["devices"]

        links = self.format_links()
        self.formatted_dict["scenario"]["links"] = links["links"]

    def format_links(self):
        links_dict = {"links": {}}
        linksList = self.input_dict["devices"] + self.input_dict["networks"]

        for i in range(len(linksList)):
            name = ""
            if linksList[i]["type"] == "RJ45":
                name = "enp0s3"
                self.links_str = self.links_str + xmltodict.unparse(
                {'link': {'@node1': "99", '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter),"@name": name},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                }, short_empty_elements=True).replace('<?xml version="1.0" encoding="utf-8"?>\n', "")
            
                links_dict["links"].update(
                {'link': {'@node1': "99", '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter),"@name": name},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                })    

            else:
                name = "eth0"
                self.links_str = self.links_str + xmltodict.unparse(
                {'link': {'@node1': "99", '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter),"@name": name, "@mac": linksList[i]["mac"], "@ip4": linksList[i]["ip"], "@ip4_mask": linksList[i]["ip4_mask"], "@ip6": "", "@ip6_mask": "64"},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                }, short_empty_elements=True).replace('<?xml version="1.0" encoding="utf-8"?>\n', "")
            
                links_dict["links"].update(
                {'link': {'@node1': "99", '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter),"@name": name, "@mac": linksList[i]["mac"], "@ip4": linksList[i]["ip"], "@ip4_mask": linksList[i]["ip4_mask"], "@ip6": "", "@ip6_mask": "64"},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                })
        return links_dict   

    def format_devices(self):
        devices_dict = {"devices": {}}
        devicesList = self.input_dict["devices"]

        for i in range(len(devicesList)):
            self.devices_str = self.devices_str + xmltodict.unparse(
                {'device': {'@id': devicesList[i]["id"], '@name': devicesList[i]["name"],
                            '@icon': "", "@canvas": "1", "@type": devicesList[i]["type"],
                            "position": self.format_position()}}, short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', "")
            devices_dict["devices"].update(
                {'device': {'@id': devicesList[i]["id"], '@name': devicesList[i]["name"],
                            '@icon': "", "@canvas": "1", "@type": devicesList[i]["type"],
                            "position": self.format_position()}})

        return devices_dict

    def format_networks(self):
        network_dict = {"networks": {}}
        networksList = self.input_dict["networks"]

        for i in range(len(networksList)):
            self.networks_str = self.networks_str + xmltodict.unparse(
                {'network': {'@id': networksList[i]["id"], '@name': networksList[i]["name"],
                             '@icon': "", "@canvas": "1", "@type": networksList[i]["type"],
                             "position": self.format_position()}}, short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', "")
            network_dict["networks"].update(
                {'network': {'@id': networksList[i]["id"], '@name': networksList[i]["name"],
                             '@icon': "", "@canvas": "1", "@type": networksList[i]["type"],
                             "position": self.format_position()}})

        self.networks_str = self.networks_str + xmltodict.unparse(
            {'network': {'@id': "99", '@name': "Switch",
                            '@icon': "", "@canvas": "1", "@type": "SWITCH",
                            "position": {'@x': "45.61198425292969", '@y': "347.94708251953125", '@lat': "47.575", "@lon": "-122.1254116826387", "@alt": "2.0"}}}, short_empty_elements=True).replace(
            '<?xml version="1.0" encoding="utf-8"?>\n', "")
        network_dict["networks"].update(
            {'network': {'@id': "99", '@name': "Switch",
                            '@icon': "", "@canvas": "1", "@type": "SWITCH",
                            "position": {'@x': "45.61198425292969", '@y': "347.94708251953125", '@lat': "47.575", "@lon": "-122.1254116826387", "@alt": "2.0"}}})
        return network_dict

    def format_position(self):
        self.id_counter += 1
        position = {'@x': "0", '@y': "0", '@lat': "47.576", "@lon": "-122." + str(1330 - (self.id_counter*5)), "@alt": "2.0"}
        return position

    def get_xml_str(self):
        return self.xml_str

    def get_networks_str(self):
        return self.networks_str
