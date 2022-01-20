# configPy [ 🏗 Under Construction ]

A tiny Configuration File Parser for Python Projects. Currently Supports JSON files only. 

## Installation

Install the Latest Stable Build - v0.0.7-Testing Build 
```
pip install configParsePy
```

## Usage 

Use configPy to get your configurations imported to your python code from JSON File.

Import the `configPy` module or the `JSONConfigParser` Object from `configPy` Module.
```
from configPy import JSONConfigParser 
```

### `JSONConfigParser` - for JSON Configuration Files


Initiate the `JSONConfigParser` by passing the JSON config file. Use `getConfigurations()` method to get the Configuration. `The getConfigurations()` method returns the configurations as a Dictionary.
```
configObject = JSONConfigParser(configFilePath="./sampleConfig.json")
configurations = configObject.getConfigurations()

OR 

configurations = JSONConfigParser(configFilePath="./sampleConfig.json").getConfigurations()
```

Use the configurations as a `dict` object.
```
print("Module Name: ", importedConfigs["module_name"])
print("Purpose: ", importedConfigs["purpose"])
```

The whole code for the above example can be found [here](./examples/jsonConfig_EXAMPLE.py).

## Examples

Usage Samples can be found in the [examples directory](./examples)
