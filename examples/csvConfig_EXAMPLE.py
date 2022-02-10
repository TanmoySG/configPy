from configPy import CSVConfigParser

importedConfigs = CSVConfigParser(configFilePath="./configFiles/sampleCSVConfig.csv").getConfigurations()

print("Sample CSVConfigParser Test")

print("Dev Environment {0} Version: ".format(importedConfigs[0]["language"]), importedConfigs[0]["version"])
print("Stage Environment {0} Version: ".format(importedConfigs[1]["language"]), importedConfigs[1]["version"])