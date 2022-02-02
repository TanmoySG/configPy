from configPy import NDJSONConfigParser

importedConfigs = NDJSONConfigParser(configFilePath="./configFiles/sampleNDJSONConfig.ndjson").getConfigurations()

print("Sample NDJSONConfigParser Test")

print("Dev Environment Python Version: ", importedConfigs[0]["version"])
print("Prod Environment Python Version: ", importedConfigs[2]["version"])

importedConfigs = NDJSONConfigParser(configFilePath="./configFiles/sampleNDJSONConfig.ndjson").mapKeysNDJSON(mappingKeys=["dev","stage","prod"]).getConfigurations()

print("Sample NDJSONConfigParser with Key Mapping Test")

print("Dev Environment Python Version: ", importedConfigs["dev"]["version"])
print("Stage Environment Python Version: ", importedConfigs["stage"]["version"])
