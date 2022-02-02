# configPy [ 🏗 Under Construction ]

A tiny Configuration File Parser for Python Projects. Currently Supports JSON files only. 

# Installation

Install the Latest Stable Build using 
```
pip install configParsePy
```

# Usage 

Use configPy to get your configurations imported to your python code from a configuration File.

Import the `configPy` module or its member methods to hadle different types of configuration files.
```
from configPy import JSONConfigParser 
```

## JSON Configuration Files

To handle JSON Configuration Files using configPy use the `JSONConfigParser` object from the configPy Module.
```
from configPy import JSONConfigParser
```
Initiate the `JSONConfigParser` by passing the JSON configuration file as an argument.
```
configObject = JSONConfigParser(configFilePath="./sampleConfig.json")
```
Use `getConfigurations()` method to get the Imported Configuration. `The getConfigurations()` method returns the configurations as a Dictionary.
```
configurations = configObject.getConfigurations()
```
Use the configurations as a `dict` object.
```
print("Module Name: ", configurations["module_name"])
print("Purpose: ", configurations["purpose"])
```
### Examples

```
from configPy import JSONConfigParser

importedConfigs = JSONConfigParser(configFilePath="./configFiles/sampleJSONConfig.json").getConfigurations()

print("Sample JSONConfigParser Test")

print("Module Name: ", importedConfigs["module_name"])
print("Purpose: ", importedConfigs["purpose"])

```
The whole code for the above example can be found [here](https://github.com/TanmoySG/configPy/blob/main/examples/jsonConfig_EXAMPLE.py).

## NDJSON Configuration Files

NDJSON or New-line Delimited JSON are files where each line is a valid JSON Object and each line is seperated by a newline `\n` character. [More about NDJSON can be found here.](http://ndjson.org/) A sample NDJSON Structure can be
```
{"env" : "dev" , "language" : "python" , "version" : 2.0}
{"env" : "stage" , "language" : "python" , "version" : 3.5}
{"env" : "prod" , "language" : "python" , "version" : 3.9}
```
Use cases for NDJSON Config Files are listed in this Issue [#11](https://github.com/TanmoySG/configPy/issues/11)

To handle NDJSON Configuration Files using configPy use the `NDJSONConfigParser` object from the configPy Module.
```
from configPy import NDJSONConfigParser
```
Initiate the `NDJSONConfigParser` by passing the configuration file as an argument.
```
configObject = NDJSONConfigParser(configFilePath="./sampleConfig.ndjson")
```
Use `getConfigurations()` method to get the Imported Configuration. `The getConfigurations()` method returns the configurations as a Dictionary.
```
configurations = configObject.getConfigurations()
```
Use the configurations as a `list` object with each JSON Object as a member of the list and can be accessed using the index number.
```
print("Dev Environment Python Version: ", importedConfigs[0]["version"])
print("Prod Environment Python Version: ", importedConfigs[2]["version"])
```

### `mapKeysNDJSON(mappingKeys=[ ])` 

While the `getCredentials()` method returns a list of JSON Objects, a user might, at times, need a key-based access to the JSON Objects ([Refer to Issue #11](https://github.com/TanmoySG/configPy/issues/11)). In such a use case the `mapKeysNDJSON()` provides the capability to map user-defined keys onto JSON Objects in the NDJSON Config files, that can be accessed using the key instead of index-number.

The `mapKeysNDJSON()` method takes an array of user defined `keys`, of length same as that of the number lines of JSON Objects in the NDJSON File. Each Key is mapped to the JSON Object of same index.
```
configObject = NDJSONConfigParser(configFilePath="./sampleNDJSONConfig.ndjson")
configurations = configObject.mapKeysNDJSON(mappingKeys=["dev","stage","prod"]).getConfigurations()
```
Using the `getConfigurations()` after using the `mapKeysNDJSON([])` method returns a `dict` object instead of a list. The imported configurations can be used by their mapped keys.
```
print("Dev Environment Python Version: ", importedConfigs["dev"]["version"])
print("Stage Environment Python Version: ", importedConfigs["stage"]["version"])
```
### Examples

```
from configPy import NDJSONConfigParser

importedConfigs = NDJSONConfigParser(configFilePath="./configFiles/sampleNDJSONConfig.ndjson").getConfigurations()

print("Sample NDJSONConfigParser Test")

print("Dev Environment Python Version: ", importedConfigs[0]["version"])
print("Prod Environment Python Version: ", importedConfigs[2]["version"])

importedConfigs = NDJSONConfigParser(configFilePath="./configFiles/sampleNDJSONConfig.ndjson").mapKeysNDJSON(mappingKeys=["dev","stage","prod"]).getConfigurations()

print("Sample NDJSONConfigParser with Key Mapping Test")

print("Dev Environment Python Version: ", importedConfigs["dev"]["version"])
print("Stage Environment Python Version: ", importedConfigs["stage"]["version"])


```
The whole code for the above example can be found [here](https://github.com/TanmoySG/configPy/blob/main/examples/ndjsonConfig_EXAMPLE.py).



