import yaml
import json

class ConfigReader:
    def database(self):
        file_path = r"C:\Users\Dell\PycharmProjects\Governata\database.json"

        with open(file_path, "r") as f:
            a = json.load(f)

        return a

