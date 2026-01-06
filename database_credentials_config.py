from config_reader import ConfigReader
print(ConfigReader.database(None)['databases']['sqlserver']['host'])
print(ConfigReader.database(None)['databases']['sqlserver']['port'])
print(ConfigReader.database(None)['databases']['sqlserver']['database'])
print(ConfigReader.database(None)['databases']['sqlserver']['username'])
print(ConfigReader.database(None)['databases']['sqlserver']['password'])



