import json, csv
import os

# Check if File Exists
def ifFileExists(filePath) -> bool:
    return os.path.exists(filePath)

# Reader Method for CSV Files. Returns Dict of JSON-Objects.
def csvReader(filePath)-> dict:

    with open(filePath, "r") as csvFileObject:
        # Read CSV as OrderedDict Objects
        csvFileDataObjects = csv.DictReader(csvFileObject)

    # Returned CSV File Data Object
    csvFileData = {}

    # Index number for CSV Rows
    csvRowIndex = 0

    for csvRowDataObject in csvFileDataObjects:

        # Convert String into JSON
        csvFileData[csvRowIndex] = dict(csvRowDataObject)

    return csvFileData


# CSVConfigParser Class - for Comma-Separated Variable (CSV) Files
class CSVConfigParser:

    # init method to initialize CSVConfigParser 
    # with file path when an object is created.
    def __init__(self, configFilePath) -> None:
        if ifFileExists(configFilePath):
            self.configFilePath = configFilePath

            # A Dictionary of separate JSON Objects is returned for CSVConfigParser. 
            # Converting the List of JSON, to dictionary with Index of JSON Object as Key.
            self.configurations = dict(enumerate(csvReader(configFilePath)))

        else:
            raise FileNotFoundError("Configuration file {0} , not found.".format(configFilePath)) 


    def mapKeysNDJSON(self, mappingKeys) -> dict:

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