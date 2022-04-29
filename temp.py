from Database import DatabaseHelper
from Models.modelClasses import Workspace


workspaces_list : list = DatabaseHelper.SDSDatabaseHelper.get_all_workspace_names()

print(workspaces_list)

workspace_obb : Workspace = DatabaseHelper.SDSDatabaseHelper.get_workspace_by_id("wosdkfjsdf")
print(workspace_obb)

print(workspace_obb.projects[2].scenarios[0].name)