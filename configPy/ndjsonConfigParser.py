from typing import Union
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


    def mapKeysNDJSON(self, mappingKeys) -> dict:

        # Raise IndexError if Length of configuration 
        # array and number of mapping keys do not match
        if len(self.configurations) != len(mappingKeys):
            raise IndexError(f"Length of Mapping Keys Array ({len(mappingKeys)}) and NDJSON Objects ({len(self.configurations)}) do not match")

        # Assign configurations list (of json objects) 
        # to a different variable - ndjsonConfigurationArray
        self.ndjsonConfigurationArray = self.configurations

        # Reassign an empty dict to configuration 
        self.configurations = {}

        # Map user-defined Keys to JSON Objects and assign to configurations variable
        for ndjsonRowNumber in range(0, len(self.ndjsonConfigurationArray)):
            self.configurations[mappingKeys[ndjsonRowNumber]] = self.ndjsonConfigurationArray[ndjsonRowNumber]

        return self

    # Return dict object if keys are mapped to JSON Objects
    # Otherwise, return list object with NDJSON Rows
    def getConfigurations(self) -> Union[list , dict]:
        return self.configurations