# open new SqlAlchemy Session and run input query.
import configparser
from typing import List
import pyodbc

from models.TableInfo import TableInfo
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class SqlServerConnection:
    # Initialize with Trusted Connection/Windows Authentication from Config File
    def __init__(self, config_section='DEFAULT'):
        self.config = configparser.ConfigParser()
        self.config_section = config_section
        self.config.read('config.ini')

        self.server = self.config[self.config_section]['server']
        self.database = self.config[self.config_section]['database']
        # This enables Windows Authentication
        self.trusted_connection = self.config[self.config_section]['trusted_connection']
        self.engine = create_engine(f'mssql+pyodbc://{self.server}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection={self.trusted_connection}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def test_connection(self):
        try:
            result = self.session.execute(text("SELECT 1"))

            print("Connection Successful")
        except Exception as e:
            print("Connection Failed")
            print(e)

if __name__ == '__main__':
    sql_conn = SqlServerConnection()
    sql_conn.test_connection()