import configparser
from typing import List

import pyodbc
import pandas as pd
import html

def open_connection(config_section='DEFAULT', database_name: str = None) -> pyodbc.Connection:
    config = configparser.ConfigParser()
    config_section = config_section
    config.read('config.ini')

    server = config[config_section]['server']
    database = database_name if database_name is not None else config[config_section]['database']
    # This enables Windows Authentication
    trusted_connection = config[config_section]['trusted_connection']

    conn = pyodbc.connect(
        f'DRIVER=ODBC Driver 17 for SQL Server;'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection={trusted_connection}'
    )

    return conn


def sanitize_params(params: dict) -> dict:
    if params is None:
        return {}
    sanitized_params = {k: html.escape(str(v)) for k, v in params.items()}
    return sanitized_params


def sql_read(file_path: str):
    with open(file_path, 'r') as file:
        sql_query = file.read().strip()
    # sql_query = sql_query.strip()
    return sql_query


def read_sql_lparams(file_path: str, database: str = None, query_params: List = None) -> pd.DataFrame:
    try:
        sql_query = sql_read(file_path)
        conn = open_connection()
        df = pd.read_sql_query(sql=sql_query, con=conn, params=query_params)
        return df
    except Exception as e:
        print("Failed to Read Sql File")
        print(e)
        raise e
    finally:
        # conn.close()
        pass


def read_sql_file(file_path: str, database: str = None, query_params: dict = None, display_query:bool = False) -> pd.DataFrame:
    try:
        sql_query = sql_read(file_path)
        conn = open_connection()
        sanitized_params = sanitize_params(query_params)
        formatted_sql_query = sql_query.format(**sanitized_params)
        if display_query:
            print(f'Executing Query:\n|{"*"*50}|\n{formatted_sql_query}\n|{"*"*50}|\n')
        df = pd.read_sql_query(sql=formatted_sql_query, con=conn)
        return df
    except Exception as e:
        print("Failed to Read Sql File")
        print(e)
        raise e
    finally:
        # conn.close()
        pass


def run_test_one():
    params = {'product_id': '805'}
    params_list = [805]
    df = read_sql_lparams("scripts/example_query_with_params.sql", query_params=params_list)
    print(df.head())


def run_test_two():
    params= {'first_name': "Tim"}
    df = read_sql_file("scripts/example_query_format_params.sql", query_params=None)
    print(df)


def run_test_two_b():
    params= {'first_name': "Tim"}
    df = read_sql_file("scripts/example_query_format_params.sql", query_params=params, display_query=True)
    print(df)

def run_test_three():
    df = read_sql_file("scripts/example_basic_query.sql")
    print(df)



def run_test_four():
    df = read_sql_file("scripts/example_basic_query.sql", display_query=True)
    print(df)


if __name__ == "__main__":
    run_test_two_b()
