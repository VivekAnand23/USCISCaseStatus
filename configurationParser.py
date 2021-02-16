import configparser

# Load configurations
properties = configparser.ConfigParser()
properties.read('config.properties')
properties.sections();

# URL to get the Case Status
CASE_STATUS_URL = properties['COMMON']['CASE_STATUS_URL']
NUMBER_OF_RECORDS = int(properties['COMMON']['NUMBER_OF_RECORDS'])
