import os
import json 
import ntpath
import sys


class File_path:
	project_root_path=os.path.dirname(os.path.dirname(__file__))
	config_file_path = project_root_path+'\\config.json'

	f = open(config_file_path, "r")
	imported_path = f.read()

	dict_obj = json.loads(imported_path)

	head, tail = ntpath.split(__file__)
	conversion_app_path = head
	conversion_app_path += "\\lib\\Conversion_App\\conversion_app.py"

	project_path = head
	lib_path = project_path + '\\lib'
	sys.path.append(lib_path)
	sys.path.append(project_path)


