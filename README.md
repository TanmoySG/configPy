# configPy [ 🏗 Under Construction ]

A tiny Configuration File Parser for Python Projects. Currently Supports JSON files only. 

## Installation

Will be Publised soon on `PyPi`. Installation instruction and documentation will be updated soon.

## Usage 

Use configPy to get your configurations imported to your python code from JSON File.


### `JSONConfigParser` - for JSON Configuration Files

Import the `JSONConfigParser` object from configPy module.
```
from config import JSONConfigParser
```

Initiate the `JSONConfigParser` by passing the JSON config file. Use `getConfigurations()` method to get the Configuration. `The getConfigurations()` method returns the configurations as a Dictionary.
```
importedConfigs = JSONConfigParser(configFilePath="./sampleConfig.json").getConfigurations()
```

Use the configurations as a `dict` object.
```
print("Module Name: ", importedConfigs["module_name"])
print("Purpose: ", importedConfigs["purpose"])
```

The whole code for the above example can be found [here](./examples/sample_jsonConfig.py).

## Examples

Usage Samples can be found in the [examples directory](./examples)
