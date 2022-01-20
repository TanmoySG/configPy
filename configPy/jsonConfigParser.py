import json
import os

# Check if File Exists
def ifFileExists(filePath) -> bool:
    return os.path.exists(filePath)


# JSONConfigParser Class - for JSON Files
class JSONConfigParser:

    # init method to initialize JSONConfigParser 
    # with file path when an object is created.

    def __init__(self, configFilePath) -> None:
        if ifFileExists(configFilePath):
            self.configFilePath = configFilePath
            self.configurations = {}
            with open(self.configFilePath, "r") as configFileObject:
                self.configurations = json.load(configFileObject)
        else:
            raise FileNotFoundError("Configuration file - {0} , not found.".format(configFilePath)) 

    def getConfigurations(self) -> dict:
        return self.configurations