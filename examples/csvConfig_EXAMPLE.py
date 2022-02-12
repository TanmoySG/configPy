from configPy import CSVConfigParser

csvConfigObject = CSVConfigParser(configFilePath="./configFiles/sampleCSVConfig.csv")
importedConfigs = csvConfigObject.getConfigurations()

print("Sample CSVConfigParser Test")

print("Dev Environment {0} Version: ".format(importedConfigs[0]["language"]), importedConfigs[0]["version"])
print("Stage Environment {0} Version: ".format(importedConfigs[1]["language"]), importedConfigs[1]["version"])

importedConfigs = csvConfigObject.mapKeys(mappingKeys=["dev","stage","prod"]).getConfigurations()

print("Sample CSVConfigParser with Key Mapping Test")

print("Dev Environment Python Version: ", importedConfigs["dev"]["version"])
print("Stage Environment Python Version: ", importedConfigs["stage"]["version"])