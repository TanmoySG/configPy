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

## Methods

### `getConfigurations()` 

The `getConfigurations()` method is used to get the Parsed Configurations from the config files. It is common for all configParser Objects.

For multi-rowed filetypes like CSV, NDJSON - the `getConfigurations()` method returns the configurations as a Dictionary with Index as Keys, for simillar usage as a List/Array (Refer to Issue [#17](https://github.com/TanmoySG/configPy/issues/17)).

```
configs = [FILETYPE]ConfigParser("[filename]").getConfigurations()
```

### `mapKeys(mappingKeys=[ ])` 

For multi-rowed filetypes like CSV, NDJSON - the `getConfigurations()` method returns a dictionary of JSON Objects that can be accessed using Index as Key. A user might, at times, need a key-based access to the JSON Objects (Refer to Issue [#11](https://github.com/TanmoySG/configPy/issues/11) and [#17](https://github.com/TanmoySG/configPy/issues/17)).

In such a use case the `mapKeys()` provides the capability to map user-defined keys onto JSON Objects in the Config files, that can be accessed using the user-assigned key instead of index-numbers.

The `mapKeys()` method takes an array of user defined `keys`, of length same as that of the number lines of JSON Objects in the Config File. Each Key is mapped to the JSON Object of same index.
```
configObject = [FILETYPE]ConfigParser(configFilePath=[filepath])
configurations = configObject.mapKeys(mappingKeys=["dev","stage","prod"]).getConfigurations()
```
Using the `getConfigurations()` after using the `mapKeys([])` method returns a `dict` object instead of a list. The imported configurations can be used by their mapped keys.
```
print("Dev Environment Python Version: ", configurations["dev"]["version"])
print("Stage Environment Python Version: ", configurations["stage"]["version"])
```

## JSON Configuration Files

To handle JSON Configuration Files using configPy use the `JSONConfigParser` object from the configPy Module. Initiate the `JSONConfigParser` by passing the JSON configuration file as an argument.

```
from configPy import JSONConfigParser
configObject = JSONConfigParser(configFilePath="./sampleConfig.json")
```
Use `getConfigurations()` method to get the Imported Configuration. `The getConfigurations()` method returns the configurations as a Dictionary. Use the configurations as a `dict` object.
```
configurations = configObject.getConfigurations()

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

To handle NDJSON Configuration Files using configPy use the `NDJSONConfigParser` object from the configPy Module. Initiate the `NDJSONConfigParser` by passing the configuration file as an argument.

```
from configPy import NDJSONConfigParser
configObject = NDJSONConfigParser(configFilePath="./sampleConfig.ndjson")
```
The `getConfigurations()` method returns the configurations as a Dictionary with Index as Keys, for simillar usage as a List/Array (Refer to Issue [#17](https://github.com/TanmoySG/configPy/issues/17)).

Use the configurations as a dictionary with each JSON Object as a member of the dict and can be accessed using the index-number as the key and can be used simillar to using a List Object.
```
configurations = configObject.getConfigurations()

print("Dev Environment Python Version: ", configurations[0]["version"])
print("Prod Environment Python Version: ", configurations[2]["version"])
```

In cases where user-defined key-mapping is required, use the `mapKeys([])`.
```
configurations = configObject.mapKeys(mappingKeys=["dev","stage","prod"]).getConfigurations()

print("Dev Environment Python Version: ", configurations["dev"]["version"])
print("Prod Environment Python Version: ", configurations["prod"]["version"])
```
### Examples

```
from configPy import NDJSONConfigParser

configObject = NDJSONConfigParser(configFilePath="./configFiles/sampleNDJSONConfig.ndjson")
importedConfigs = configObject.getConfigurations()

print("Sample NDJSONConfigParser Test")

print("Dev Environment Python Version: ", importedConfigs[0]["version"])
print("Prod Environment Python Version: ", importedConfigs[2]["version"])

importedConfigs = configObject.mapKeys(mappingKeys=["dev","stage","prod"]).getConfigurations()

print("Sample NDJSONConfigParser with Key Mapping Test")

print("Dev Environment Python Version: ", importedConfigs["dev"]["version"])
print("Stage Environment Python Version: ", importedConfigs["stage"]["version"])

```
The whole code for the above example can be found [here](https://github.com/TanmoySG/configPy/blob/main/examples/ndjsonConfig_EXAMPLE.py).


## CSV Configuration Files

CSV or Comma-Seperated Variable Files are a common means of storing data and configurations.

To handle CSV Configuration Files using configPy use the `CSVConfigParser` object from the configPy Module. Initiate the `CSVConfigParser` by passing the configuration file as an argument.

```
from configPy import CSVConfigParser

configObject = CSVConfigParser(configFilePath="./sampleConfig.csv")
```
The `getConfigurations()` method returns the configurations as a Dictionary with Index as Keys, for simillar usage as a List/Array (Refer to Issue [#15](https://github.com/TanmoySG/configPy/issues/15)).

Use the configurations as a dictionary with each JSON Object as a member of the dict and can be accessed using the index-number as the key and can be used simillar to using a List Object.
```
configurations = configObject.getConfigurations()

print("Dev Environment Python Version: ", configurations[0]["version"])
print("Prod Environment Python Version: ", configurations[2]["version"])
```

In cases where user-defined key-mapping is required, use the `mapKeys([])`.
```
configurations = configObject.mapKeys(mappingKeys=["dev","stage","prod"]).getConfigurations()

print("Dev Environment Python Version: ", configurations["dev"]["version"])
print("Prod Environment Python Version: ", configurations["prod"]["version"])
```
### Examples

```
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
```
The whole code for the above example can be found [here](https://github.com/TanmoySG/configPy/blob/main/examples/csvConfig_EXAMPLE.py).
