from configPy import NDJSONConfigParser
import unittest


class NDJSONConfigParserTestCase(unittest.TestCase):

    # Success Case -
    # If File exists the JSONConfigParser Object should
    # return the content of the Existing JSON Config File
    def test_NDJSONConfigParser_successCase(self):
        importedConfigs = NDJSONConfigParser(
            configFilePath="./tests/configFiles/sampleNDJSONConfig.ndjson").getConfigurations()

        idealCaseConfigs = {
            0: {"env": "dev", "language": "python", "version": 2.0},
            1: {"env": "stage", "language": "python", "version": 3.5},
            2: {"env": "prod", "language": "python", "version": 3.9}
        }

        self.assertEqual(importedConfigs, idealCaseConfigs)

    # File Does Not Exist Case -
    # Raises 'FileNotFoundError' Exception when file doesn't exist

    def test_NDJSONConfigParser_fileMissingCase(self):
        self.assertRaises(FileNotFoundError, NDJSONConfigParser,
                          "./configFiles/samplJSONConfig.json")

    def test_NDJSONConfigParser_KeyMappingCase(self):
        filePath = "./tests/configFiles/sampleNDJSONConfig.ndjson"
        importedConfigs = NDJSONConfigParser(configFilePath=filePath).mapKeys(mappingKeys=["dev", "stage", "prod"]).getConfigurations()

        self.assertEqual(importedConfigs["dev"]["version"], 2.0)
        self.assertEqual(importedConfigs["stage"]["env"], "stage")
        self.assertEqual(importedConfigs["prod"]["language"], "python")


if __name__ == '__main__':
    unittest.main()
