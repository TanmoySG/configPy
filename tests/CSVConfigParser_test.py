from configPy import CSVConfigParser
import unittest


class CSVConfigParserTestCase(unittest.TestCase):

    # Success Case -
    # If File exists the JSONConfigParser Object should
    # return the content of the Existing JSON Config File
    def test_NDJSONConfigParser_successCase(self):
        filepath = "./tests/configFiles/sampleCSVConfig.csv"
        importedConfigs = CSVConfigParser(configFilePath=filepath).getConfigurations()

        idealCaseConfigs = {
            0: {"env": "dev", "language": "python", "version": "3.5"},
            1: {"env": "stg", "language": "java", "version": "4.5"},
            2: {"env": "prod", "language": "golang", "version": "2.4"}
        }

        self.assertEqual(importedConfigs, idealCaseConfigs)

    # File Does Not Exist Case -
    # Raises 'FileNotFoundError' Exception when file doesn't exist

    def test_NDJSONConfigParser_fileMissingCase(self):
        self.assertRaises(FileNotFoundError, CSVConfigParser,
                          "./configFiles/samplJSONConfig.json")

    def test_NDJSONConfigParser_KeyMappingCase(self):
        filepath = "./tests/configFiles/sampleCSVConfig.csv"
        importedConfigs = CSVConfigParser(configFilePath=filepath).mapKeys(mappingKeys=["dev", "stage", "prod"]).getConfigurations()

        self.assertEqual(importedConfigs["dev"]["version"], "3.5")


if __name__ == '__main__':
    unittest.main()
