import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Get the names of all sections
section_names = config.sections()
section_names.insert(0, 'DEFAULT')
print(section_names)