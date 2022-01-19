from config import JSONConfigParser

importedConfigs = JSONConfigParser(
    configFilePath="./sampleConfig.json").getConfigurations()

print("Sample JSONConfigParser Test")

print("Module Name: ", importedConfigs["module_name"])
print("Purpose: ", importedConfigs["purpose"])
