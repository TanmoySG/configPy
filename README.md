# configPy [ 🏗 Under Construction ]

A tiny Configuration File Parser for Python Projects. Currently Supports JSON files only. 

## Installation

Will be Publised soon on `PyPi`. Installation instruction and documentation will be updated soon.

## Usage 

Use configPy to get your configurations imported to your python code from JSON File.

```
from config import JSONConfigParser

importedConfigs = JSONConfigParser(configFilePath="./sampleConfig.json").getConfigurations()

print("Module Name: ", importedConfigs["module_name"])
print("Purpose: ", importedConfigs["purpose"])
```

## Examples

Usage Samples can be found in the [examples directory](./examples)
