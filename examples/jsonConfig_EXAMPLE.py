from configPy import JSONConfigParser

importedConfigs = JSONConfigParser(configFilePath="./configFiles/sampleJSONConfig.json").getConfigurations()

print("Sample JSONConfigParser Test")

print("Module Name: ", importedConfigs["module_name"])
print("Purpose: ", importedConfigs["purpose"])
