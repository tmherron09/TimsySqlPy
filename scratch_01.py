import configparser
from typing import List

import pyodbc

from models.TableInfo import TableInfo


class SqlUtil:
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


    def get_all_tables(self, database:str = None, store_table_info=False, print_tables_info=False):
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


    def get_all_sql_columns(self, store_column_info=False, print_column_info=False):
        sql_query = """
        SELECT *
        FROM sys.columns
        """

        # Re-Open Connection
        self.open_connection()

        # Execute the query
        cursor = self.conn.cursor()
        cursor.execute(sql_query)

        # Fetch the results
        rows: List[pyodbc.Row] = cursor.fetchall()

        if store_column_info:
            self.all_column_info: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(self.all_column_info) == 0 else len(self.all_column_info)
                self.all_column_info.insert(curr_indx, TableInfo(*row))
            if print_column_info:
                self.print_tables_info(self.all_column_info)
        elif store_column_info != True & print_column_info == True:
            all_column_info_in_mem: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(all_column_info_in_mem) == 0 else len(all_column_info_in_mem)
                all_column_info_in_mem.insert(curr_indx, TableInfo(*row))
            self.print_all_tables_info(all_column_info_in_mem)
        self.conn.close()


    def get_all_sql_columns_for_table(self, table_name: str, store_column_info=False, print_column_info=False):
        sql_query = f"""
        SELECT *
        FROM sys.columns
        WHERE object_id = OBJECT_ID('{table_name}')
        """

        # Re-Open Connection
        self.open_connection()

        # Execute the query
        cursor = self.conn.cursor()
        cursor.execute(sql_query)

        # Fetch the results
        rows: List[pyodbc.Row] = cursor.fetchall()

        if store_column_info:
            self.all_column_info: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(self.all_column_info) == 0 else len(self.all_column_info)
                self.all_column_info.insert(curr_indx, TableInfo(*row))
            if print_column_info:
                self.print_tables_info(self.all_column_info)
        elif store_column_info != True & print_column_info == True:
            all_column_info_in_mem: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(all_column_info_in_mem) == 0 else len(all_column_info_in_mem)
                all_column_info_in_mem.insert(curr_indx, TableInfo(*row))
            self.print_all_tables_info(all_column_info_in_mem)
        self.conn.close()

    def get_all_references_for_column(self, column_name: str, store_column_info=False, print_column_info=False):
        sql_get_referenced_entities = f"""
        SELECT *
        FROM sys.dm_sql_referenced_entities('{column_name}', 'OBJECT')
        """
        # Re-Open Connection
        self.open_connection()

        # Execute the query
        cursor = self.conn.cursor()
        cursor.execute(sql_get_referenced_entities)

        # Fetch the results
        rows: List[pyodbc.Row] = cursor.fetchall()

        if store_column_info:
            self.all_column_info: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(self.all_column_info) == 0 else len(self.all_column_info)
                self.all_column_info.insert(curr_indx, TableInfo(*row))
            if print_column_info:
                self.print_tables_info(self.all_column_info)
        elif store_column_info != True & print_column_info == True:
            all_column_info_in_mem: List[TableInfo] = []
            for row in rows:
                curr_indx = 0 if len(all_column_info_in_mem) == 0 else len(all_column_info_in_mem)
                all_column_info_in_mem.insert(curr_indx, TableInfo(*row))
            self.print_all_tables_info(all_column_info_in_mem)
        self.conn.close()

    def print_all_tables_info(self, all_tables_info: List[TableInfo]):
        print(f"Printing Tables Info for {self.database}")
        print(f"There are {len(all_tables_info)} tables.")
        for table in all_tables_info:
            print(table)


if __name__ == "__main__":
    sql_util = SqlUtil()
    sql_util.get_all_tables()

