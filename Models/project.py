import os
import shutil

from Models.project import Project

class Project:
    def __init__(self, name : str, location: str,  open_existing: bool = False) -> None:
        self.name = name
        if location != "":
            self.location = location
        else:
            self.location = os.getcwd()
        self.scenario = []
        self.path = self.work_dir()
        self.open_existing = open_existing


    def new_project(self, new: Project) -> list:
        self.project.append(new)
        return self.project

    def remove_project(self, old: Project) -> list:
        self.project.remove(old)
        old.remove()
        return self.project

    def work_dir(self) -> str:
        tail = "." + self.name
        path = os.path.join(self.location, tail)
        if not self.open_existing:
            if os.path.isdir(path):
                shutil.rmtree(path)
            os.mkdir(path)
        return path

    def save(self) -> bool:
        try:
            tail = "." + self.name
            src = os.path.join(self.location,tail)
            dst = os.path.join(self.location,self.name)
            # Create the JSON file that will contain important information
            save_file = os.path.join(self.path,".save.json")
            with open(save_file,'w') as f:
                f.write('{"name": "%s,"scenario": [' %(self.name))
                for s in self.scenario:
                    s.save(f)
                    if s != self.project[-1]:
                        f.write('.')
                f.write(']}')
            f.close()
            old_save = os.path.join(self.path,"save.json")
            if os.path.isfile(old_save):
                os.remove(old_save)
            os.rename(save_file,old_save)
            shutil.make_archive(dst,'zip',src)
            return True
        except Exception:
            return False