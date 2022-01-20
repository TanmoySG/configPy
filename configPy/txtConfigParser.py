import os

# Check if File Exists
def ifFileExists(filePath) -> bool:
    return os.path.exists(filePath)


# TXTConfigParser Class - for TXT Files
class TXTConfigParser:

    # init method to initialize TXTConfigParser 
    # with file path when an object is created.

    def __init__(self, configFilePath) -> None:
        self.configurations = {"file_type" : "TXT", "input" : configFilePath}

        # Usage Mechanism TBD 

        # Sample Code -

        # if ifFileExists(configFilePath):
        #     self.configFilePath = configFilePath
        #     self.configurations = {}
        #     with open(self.configFilePath, "r") as configFileObject:
        #         self.configurations = json.load(configFileObject)
        # else:
        #     raise FileNotFoundError("Configuration file - {0} , not found.".format(configFilePath)) 

    def getConfigurations(self) -> dict:
        return self.configurations