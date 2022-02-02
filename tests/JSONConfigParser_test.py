import json
import unittest
from configPy import JSONConfigParser

class JSONConfigParserTestCase(unittest.TestCase):

    # Success Case - 
    # If File exists the JSONConfigParser Object should 
    # return the content of the Existing JSON Config File
    def test_JSONConfigParser_successCase(self):
        importedConfigs = JSONConfigParser(configFilePath="./tests/configFiles/sampleJSONConfig.json").getConfigurations()

        with open("./tests/configFiles/sampleJSONConfig.json", "r") as IdealCaseObj:
            idealCaseConfigs = json.load(IdealCaseObj)

        self.assertEqual(importedConfigs, idealCaseConfigs)


    # File Does Not Exist Case - 
    # Raises 'FileNotFoundError' Exception when file doesn't exist
    def test_JSONConfigParser_fileMissingCase(self):
        self.assertRaises(FileNotFoundError, JSONConfigParser, "./samplConfig.json" )
        
if __name__ == '__main__':
    unittest.main()
