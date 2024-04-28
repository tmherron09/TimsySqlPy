import configparser
from typing import List

import pyodbc
import pandas as pd

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

    @staticmethod
    def read_sql_file(file_path: str):
        with open(file_path, 'r') as file:
            sql_query = file.read()
        return sql_query


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
                self.print_all_tables_info(self.all_table_info)
        elif not store_table_info & print_tables_info:
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

    @staticmethod
    def print_rows(rows: List[pyodbc.Row]):
        for idx, row in enumerate(rows):
            print(idx, ":", row)

    def execute_sql_file(self, file_path: str, database: str = None):
        try:
            sql_query = self.read_sql_file(file_path)
            self.open_connection()
            cursor = self.conn.cursor()
            cursor.execute(sql_query)
            rows: List[pyodbc.Row] = cursor.fetchall()
            self.conn.commit()
            return rows
        except Exception as e:
            print(e)
            raise e
        finally:
            self.conn.close()

    def sql_file_to_df(self, file_path: str, database: str = None):
        try:
            sql_query = self.read_sql_file(file_path)
            self.open_connection()
            df = pd.read_sql(sql_query, self.conn)
            return df
        except Exception as e:
            print(e)
            raise e
        finally:
            self.conn.close()


if __name__ == "__main__":
    sql_util = SqlUtil()
    # sql_util.get_all_tables()
    result = sql_util.execute_sql_file('scripts/example_basic_query.sql')
    sql_util.print_rows(result)

    pd_result = sql_util.sql_file_to_df('scripts/example_basic_query.sql')
    print(pd_result)