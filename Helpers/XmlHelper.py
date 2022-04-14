#! /usr/bin/env python3
import xmltodict
import os

# Helper class to create an xml string from a given dictionary.
# Node IDs must be larger than 10 (this allows a max of 10 switches or subnets, if more are required then make sure the node ids are large)
# IDs must be base10
# RJ45 can be created but not tested, from my understanding RJ45 will only be used for docker.
# Please follow the given convention {"name": "ScenarioA", #any name will do
#               "networks":[
#                 #   {"id": "12", # for all ids they must be greated than 10, this allows for at least 10 switches if we want more make sure the ids start with a larger number
#                 #    "name": "Docker",
#                 #    "type": "RJ45",
#                 #    "mac": "aa:aa:aa:aa:aa:aa",
#                 #    "ip": "10.10.10.10",
#                 #    "ip4_mask": "24"},
#                   ],
#               "devices":[ # Core would be of type PC
#                   {"id": "14",
#                    "name": "n1s1",
#                    "type": "PC",
#                    "mac": "aa:aa:aa:aa:aa:ac",
#                    "ip": "10.10.1.2",
#                    "ip4_mask": "24"}]}
# networks refers to RJ45 nodes
# devices refers to core nodes such as Core or victims
# all mac, ips, and ids must be unique 
class XmlHelper:
    
    # Default config for all nodes. Custome services can also be assigned by node.
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
    routerLinkips= []

    link_dict = {}

    # Constcutor to create helper class object, methods were included to reduce the number of calls. Creating an object will do everything and lastly you would just have to get the string or file.
    def __init__(self, input_dict):
        self.input_dict = input_dict
        self.format_dict()
        self.create_xml_string()
        self.create_xml_file()

    # method used to replace strings it created xml string. This is required due to the library limitation that can only transform dictionary to xml. Since dictionaries dont allow duplicated i must do this to force duplicate keys.
    def replace_key_XML(self, new_str, old_str):
        self.xml_str = self.xml_str.replace(new_str, old_str)

    # callable method used to create a string from using the dictionary provided to the obj
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

    # callable method used to create an xml file
    def create_xml_file(self):
        xmlfile = open(f"{self.input_dict['name']}.xml", "w")
        xmlfile.write(self.xml_str)
        xmlfile.close()

    # main method that initiates the whole xml creation process 
    def format_dict(self):
        self.find_subnets()
        self.formatted_dict = {"scenario": {'@name': os.getcwd() + f'\{self.input_dict["name"]}'}}

        networks = self.format_networks()
        self.formatted_dict["scenario"]["networks"] = networks["networks"]

        if len(self.input_dict["devices"]) > 0:
            devices = self.format_devices()
            self.formatted_dict["scenario"]["devices"] = devices["devices"]

        links = self.format_links()
        self.formatted_dict["scenario"]["links"] = links["links"]

    # uses given dictionary to find subnets, build links, and creat ID for new switches
    def find_subnets(self):
        self.link_dict
        for node in self.input_dict["devices"]+self.input_dict["networks"]:
            ip_split = node['ip'].split(".")
            subnet = ip_split[0] + "." + ip_split[1] + "." + ip_split[2]
            originalIP = subnet + ".1"
            subnet = subnet.replace(".","")
            if subnet in self.link_dict:
                node["link"] = subnet
                self.link_dict[subnet].append(node["id"])
            else:
                node["link"] = subnet
                self.link_dict[subnet] = [node["id"]]
                self.routerLinkips.append(originalIP)
        return self.link_dict

    # Method to format all links of the scenario. This includes PCs, RJ45, switches, and router
    def format_links(self):
        links_dict = {"links": {}}
        linksList = self.input_dict["devices"] + self.input_dict["networks"]
        ethCount = 0
        for i in range(len(linksList)):
            name = ""
            if linksList[i]["type"] == "RJ45":
                name = "enp0s3"
                self.links_str = self.links_str + xmltodict.unparse(
                {'link': {'@node1': linksList[i]["link"], '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter+100),"@name": name},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                }, short_empty_elements=True).replace('<?xml version="1.0" encoding="utf-8"?>\n', "")
            
                links_dict["links"].update(
                {'link': {'@node1': linksList[i]["link"], '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter+100),"@name": name},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                })    

            elif linksList[i]["type"] == "PC":
                name = "eth0"
                self.links_str = self.links_str + xmltodict.unparse(
                {'link': {'@node1': linksList[i]["link"], '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter+100),"@name": name, "@mac": linksList[i]["mac"], "@ip4": linksList[i]["ip"], "@ip4_mask": linksList[i]["ip4_mask"], "@ip6": "", "@ip6_mask": "64"},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                }, short_empty_elements=True).replace('<?xml version="1.0" encoding="utf-8"?>\n', "")
            
                links_dict["links"].update(
                {'link': {'@node1': linksList[i]["link"], '@node2': linksList[i]["id"],"iface2":{"@id":str(self.id_counter+100),"@name": name, "@mac": linksList[i]["mac"], "@ip4": linksList[i]["ip"], "@ip4_mask": linksList[i]["ip4_mask"], "@ip6": "", "@ip6_mask": "64"},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                })
            elif linksList[i]["type"] == "SWITCH":
                name = "eth" + str(ethCount)
                self.links_str = self.links_str + xmltodict.unparse(
                {'link': {'@node1': linksList[i]["id"], '@node2': "999","iface2":{"@id":str(self.id_counter+1000),"@name": name, "@ip4": linksList[i]["ip"], "@ip4_mask": linksList[i]["ip4_mask"], "@ip6": "2001::1", "@ip6_mask": "64"},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                }, short_empty_elements=True).replace('<?xml version="1.0" encoding="utf-8"?>\n', "")
            
                links_dict["links"].update(
                {'link': {'@node1': linksList[i]["id"], '@node2': "999","iface2":{"@id":str(self.id_counter+1000),"@name": name, "@ip4": linksList[i]["ip"], "@ip4_mask": linksList[i]["ip4_mask"], "@ip6": "2001::1", "@ip6_mask": "64"},
                "options":{"@delay": "0", "@bandwith": "0", "@loss": "0.0", "@dup": "0", "@jitter": "0", "@unidirectional": "0", "@buffer": "0"}}
                })
                self.id_counter += 1
                ethCount += 1
            else: continue
        return links_dict   
    
    # formated the PC nodes as well as the router that all switches are connected to
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

        self.devices_str = self.devices_str + xmltodict.unparse(
            {'device': {'@id': "999", '@name': "R",
                            '@icon': "", "@canvas": "1", "@type": "router" , "@class" : "", "@image" : "",
                            "position": {'@x': "385.54595947265625", '@y': "545.1220703125", '@lat': "47.57421120379505", "@lon": "-122.12712909132811", "@alt": "2.0"}}}, short_empty_elements=True).replace(
            '<?xml version="1.0" encoding="utf-8"?>\n', "")
        devices_dict["devices"].update(
            {'device': {'@id': "999", '@name': "R",
                            '@icon': "", "@canvas": "1", "@type": "router", "@class" : "", "@image" : "",
                            "position": {'@x': "385.54595947265625", '@y': "545.1220703125", '@lat': "47.57421120379505", "@lon": "-122.12712909132811", "@alt": "2.0"}}})

        return devices_dict

    # method to format RJ45 nodes, in additon it uses the subnet information to create the required number of switches
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

        count = 1
        ip = 0
        for switch in self.link_dict:
            self.id_counter += 1
            self.input_dict["networks"].append({"id":switch,"name": "s"+ str(count), "link": "999", "type" : "SWITCH", "ip": self.routerLinkips[ip], "ip4_mask": "24", "ip6":"", "ip6_mask":"64"})    
            self.networks_str = self.networks_str + xmltodict.unparse(
                {'network': {'@id': switch, '@name': "s"+ str(count),
                                '@icon': "", "@canvas": "1", "@type": "SWITCH",
                                "position": {'@x': "258.0612487792969", '@y': "388.3501281738281", '@lat': "47.57563632286221", "@lon": "-122." + str(132 - (self.id_counter)), "@alt": "2.0"}}}, short_empty_elements=True).replace(
                '<?xml version="1.0" encoding="utf-8"?>\n', "")
            network_dict["networks"].update(
                {'network': {'@id': switch, '@name': "s"+ str(count),
                                '@icon': "", "@canvas": "1", "@type": "SWITCH",
                                "position": {'@x': "258.0612487792969", '@y': "388.3501281738281", '@lat': "47.57563632286221", "@lon": "-122." + str(132 - (self.id_counter)), "@alt": "2.0"}}})
            count += 1
            ip += 1
        return network_dict

    # method to format the postion of
    def format_position(self):
        self.id_counter += 1
        position = {'@x': "0", '@y': "0", '@lat': "47.57792708883367", "@lon": "-122." + str(1330 - (self.id_counter*5)), "@alt": "2.0"}
        return position

    # getter to obtain created xml string
    def get_xml_str(self):
        return self.xml_str

    # method used for testing. to see what type of information was being saved.
    def get_networks_str(self):
        return self.networks_str

# example of dictionary needed
# the arrays can be blank if needed.

test_input = {"name": "ScenarioA", #any name will do
              "networks":[
                #   {"id": "12", # for all ids they must be greated than 10, this allows for at least 10 switches if we want more make sure the ids start with a larger number
                #    "name": "Docker",
                #    "type": "RJ45",
                #    "mac": "aa:aa:aa:aa:aa:aa",
                #    "ip": "10.10.10.10",
                #    "ip4_mask": "24"},
                  ],
              "devices":[ # Core would be of type PC
                  {"id": "14",
                   "name": "n1s1",
                   "type": "PC",
                   "mac": "aa:aa:aa:aa:aa:ac",
                   "ip": "10.10.1.2",
                   "ip4_mask": "24"},
                   {"id": "15",
                   "name": "n2s1",
                   "type": "PC",
                   "mac": "aa:aa:aa:aa:aa:ae",
                   "ip": "10.10.1.3",
                   "ip4_mask": "24"},
                    {"id": "16",
                   "name": "n3s1",
                   "type": "PC",
                   "mac": "aa:aa:aa:aa:aa:ad",
                   "ip": "10.10.1.4",
                   "ip4_mask": "24"},
                   {"id": "17",
                   "name": "n4s2",
                   "type": "PC",
                   "mac": "aa:aa:aa:aa:aa:af",
                   "ip": "10.10.2.2",
                   "ip4_mask": "24"},
                    {"id": "18",
                   "name": "n5s2",
                   "type": "PC",
                   "mac": "aa:aa:aa:aa:aa:1c",
                   "ip": "10.10.2.4",
                   "ip4_mask": "24"},
                   {"id": "19",
                   "name": "n6s2",
                   "type": "PC",
                   "mac": "aa:aa:aa:aa:aa:1e",
                   "ip": "10.10.2.3",
                   "ip4_mask": "24"}
                  ]
              }
