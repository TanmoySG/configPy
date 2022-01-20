from configPy import *

print(TXTConfigParser("hi").getConfigurations())
print(JSONConfigParser("./sampleConfig.json").getConfigurations())