import json


class Configuration:
    __instance = None
    path = ""

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Configuration.__instance is None:
            Configuration()
        return Configuration.__instance

    configuration = {}

    def __init__(self):
        if Configuration.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Configuration.__instance = self

        self.load("config.json")

    def load(self, path):
        self.path = path
        with open(path) as json_data_file:
            self.configuration = json.load(json_data_file)

        print(self.configuration)

    def get_project_path(self):
        return self.configuration["project_path"]

    def get_external_path(self):
        return self.configuration["external_path"]

    def get_app_name(self):
        return "Texas"

    def get_editor_theme(self):
        return self.configuration["editor_theme"]

    def set_editor_theme(self, name):
        if name == self.get_editor_theme():
            return
        if name in ["vs", "vs-dark","hc-black"]:
            self.__replace_json_value("editor_theme", name)

        self.configuration["editor_theme"] = name


    def __replace_json_value(self, key, value):
        with open(self.path) as infile:
            data = json.load(infile)

        data[key] = value

        with open(self.path, 'w') as outfile:
            json.dump(data, outfile)

        # to be modified - new lines are not written
