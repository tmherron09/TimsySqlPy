import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'server': 'INSERTHERE',
    'database': 'AdventureWorks2022',
    'trusted_connection': 'yes'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)