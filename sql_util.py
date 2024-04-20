import configparser
from typing import List

import pyodbc

from models.TableInfo import TableInfo


class SqlUtil():
    def __init__(self, config_section='DEFAULT'):
        self.config = configparser.ConfigParser()
        self.config_section = config_section
        self.config.read('config.ini')

        self.server = self.config[self.config_section]['server']
        self.database = self.config[self.config_section]['database']
        # This enables Windows Authentication
        self.trusted_connection = self.config[self.config_section]['trusted_connection']

    def open_connection(self, database=None):
        if database is not None:
            self.database = database

        self.conn: pyodbc.Connection = pyodbc.connect(
            f'DRIVER=ODBC Driver 17 for SQL Server;'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'Trusted_Connection={self.trusted_connection}'
        )

    def update_server(self, server):
        self.server = server

    def _execute_query(self, query_func, database=None):
        self.open_connection(database)
        try:
            result = query_func()

            return result
        except:
            # Currently Not Executing Script that can be RolledBack
            # Expected Read/Query Only Access
            # session.rollback()
            raise
        finally:
            self.conn.close()



    def get_all_tables(self, database: str = None, store_table_info=False, print_tables_info=False):
        sql_query = """
        SELECT *
        FROM sys.tables
        """

        # Re-Open Connection
        self.open_connection(database)

        # Execute the query
        cursor = self.conn.cursor()
        cursor.execute(sql_query)

        # Fetch the results
        rows: List[pyodbc.Row] = cursor.fetchall()

        if store_table_info:
            self.all_table_info: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(self.all_table_info) == 0 else len(self.all_table_info)
                self.all_table_info.insert(curr_indx, TableInfo(*row))
            if print_tables_info:
                self.print_tables_info(self.all_table_info)
        elif store_table_info != True & print_tables_info == True:
            all_table_info_in_mem: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(all_table_info_in_mem) == 0 else len(all_table_info_in_mem)
                all_table_info_in_mem.insert(curr_indx, TableInfo(*row))
            self.print_all_tables_info(all_table_info_in_mem)
        self.conn.close()

    def print_all_tables_info(self, all_tables_info: List[TableInfo]):
        print(f"Printing Tables Info for {self.database}")
        print(f"There are {len(all_tables_info)} tables.")
        for table in all_tables_info:
            print(table)


if __name__ == "__main__":
    sql_util = SqlUtil()
    sql_util.get_all_tables()
