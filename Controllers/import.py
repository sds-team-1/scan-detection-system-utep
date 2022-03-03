

from Models.project import Project, Scenario

import json, datetime, os, shutil

class Load:
    def __init__(self):
        self.project = None

    def load_project(self, path:str) -> Project:
        try:
            head, tail = os.path.split(path)
            with open(os.path.join(path, 'save.json')) as f:
                data = f.read()
            js = json.loads(data)
            if tail[1:] == js['name']:
                w = Project(js['name'],head, open_existing = True)
                self.load_scenario(w,js['scenario'])
            else:
                w = None
            return w
        except FileNotFoundError:
            print("File not Found")
            shutil.rmtree(path)
            return None
        except Exception:
            print("Unable to read file")
            shutil.rmtree(path)
            return None

    def load_scenario(self, project: Project, scenarios: list) -> list:
        for s in scenarios:
            scen = Scenario(s['name'],project.path,s['create_time'])
            self.load_node(scen,s['node'])
            project.new_scenario(scen)

        return
    def load_node(self):
        return
    def load_capture(self):
        return
    def load_pcap(self):
        return
    def import_zip(self,path:str)-> Project:
        try:
            if not os.path.isfile(path):
                raise Exception
            root, ext = os.path.splitext(path)
            if ext.lower() != ".zip":
                raise Exception
            head, tail = os.path.split(root)
            tail = "." + tail
            working_dir = os.path.join(head,tail)
            if os.path.isdir(working_dir):
                shutil.rmtree(working_dir)
            shutil.unpack_archive(path,working_dir)
            return self.load_project(working_dir)
        except Exception:
            print("error opening zip file")
            return None
