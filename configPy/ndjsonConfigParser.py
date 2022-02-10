import json
import os

# Check if File Exists
def ifFileExists(filePath) -> bool:
    return os.path.exists(filePath)

# Reader Method for NDJSON Files. Returns list of JSON-Objects.
def ndjsonReader(filePath)-> list:

    with open(filePath, "r") as ndjsonFileObject:

        # Parse NDJSON File
        ndjsonFileData = ndjsonFileObject.read().split("\n")

    for JSONStringIndex in range(0, len(ndjsonFileData)):

        # Convert String into JSON
        convertedJSONLine = json.loads(ndjsonFileData[JSONStringIndex])

        # Replace JSON String by JSON Object
        ndjsonFileData[JSONStringIndex] = convertedJSONLine

    return ndjsonFileData


# NDJSONConfigParser Class - for Newline-Delimited JSON Files
class NDJSONConfigParser:

    # init method to initialize NDJSONConfigParser 
    # with file path when an object is created.
    def __init__(self, configFilePath) -> None:
        if ifFileExists(configFilePath):
            self.configFilePath = configFilePath

            # A Dictionary of separate JSON Objects is returned for NDJsonConfigParser. 
            # Converting the List of JSON, to dictionary with Index of JSON Object as Key.
            self.configurations = dict(enumerate(ndjsonReader(configFilePath)))

        else:
            raise FileNotFoundError("Configuration file {0} , not found.".format(configFilePath)) 


    def mapKeys(self, mappingKeys) -> dict:

        # Raise IndexError if Length of configuration 
        # array and number of mapping keys do not match
        if len(self.configurations.keys()) != len(mappingKeys):
            raise IndexError(f"Length of Mapping Keys Array ({len(mappingKeys)}) and NDJSON Objects ({len(self.configurations)}) do not match")

        # Map user-defined Keys to JSON Objects and assign to configurations variable
        for ndjsonRowNumber in self.configurations.keys():
            self.configurations[mappingKeys[ndjsonRowNumber]] = self.configurations.pop(ndjsonRowNumber)

        return self

    # Return dict object if keys are mapped to JSON Objects
    # Otherwise, return list object with NDJSON Rows
    def getConfigurations(self) -> dict:
        return self.configurations