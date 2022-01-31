import json
import os

# Check if File Exists
def ifFileExists(filePath) -> bool:
    return os.path.exists(filePath)

# Reader Method for NDJSON Files. Returns list of JSON (as String).
def ndjsonReader(filePath)-> list:
    with open(filePath, "r") as ndjsonFileObject:
        ndjsonFileData = ndjsonFileObject.read().split("\n")

    return ndjsonFileData


# NDJSONConfigParser Class - for Newline-Delimited JSON Files
class NDJSONConfigParser:

    # init method to initialize NDJSONConfigParser 
    # with file path when an object is created.

    def __init__(self, configFilePath) -> None:
        if ifFileExists(configFilePath):
            self.configFilePath = configFilePath

            # A List of separate JSON Objects / Dicts
            # are returned for NDJsonConfigParser.
            self.configurations = []

            # Using ndjsonReader Method to read the NDJSON File
            for JSONLine in ndjsonReader(configFilePath):

                # ndjsonReader method returns a list of JSON Objects as strings
                # The Strings are converted into JSON Objects using json.loads()
                convertedJSONLine = json.loads(JSONLine)

                # Append converted JSON Objects to the configurations (list in case of NDJSON)
                self.configurations.append(convertedJSONLine)
        else:
            raise FileNotFoundError("Configuration file {0} , not found.".format(configFilePath)) 

    def getConfigurations(self) -> list:
        return self.configurations