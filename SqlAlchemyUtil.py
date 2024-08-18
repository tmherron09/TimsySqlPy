import configparser
from typing import Sequence, Any

from sqlalchemy import create_engine, text, Engine, CursorResult, Row
from sqlalchemy.orm import sessionmaker, Session, Query, declarative_base
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.schema import CreateTable
import pandas as pd

Base = declarative_base()

class User(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class SqlAlchemyUtil:
    def __init__(self, config_section='DEFAULT'):
        self.config = configparser.ConfigParser()
        self.config_section = config_section
        self.config.read('config.ini')

        self.server = self.config[self.config_section]['server']
        self.database = self.config[self.config_section]['database']
        # This enables Windows Authentication
        self.trusted_connection = self.config['DEFAULT'].getboolean('trusted_connection')

        if self.trusted_connection:
            # connection_string = f'mssql+pyodbc://{self.server}/{self.database}?trusted_connection=yes'
            connection_string = f'mssql+pyodbc://{self.server}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection={self.trusted_connection}'
        else:
            # If not using trusted connection, also provide username and password
            self.username = self.config['DEFAULT']['username']
            self.password = self.config['DEFAULT']['password']
            connection_string = f'mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}'

        self.engine: Engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)


    def _execute_query(self, query_func):
        session = self.Session()
        try:
            cursor_result: CursorResult = query_func(session)
            result = cursor_result.all()
            session.commit()
            return result
        except:
            # Currently Not Executing Script that can be RolledBack
            # Expected Read/Query Only Access
            # session.rollback()
            raise
        finally:
            session.close()

    def example_basic_query(self):
        def query_func(session):
            with open('scripts/example_basic_query.sql', 'r') as file:
                sql_query = file.read()
            cursor = session.execute(text(sql_query))
            return cursor


        return self._execute_query(query_func)

    def query_all_tables(self):
        def query_func(session: Session):
            # Your query logic goes here

            metadata = MetaData()
            # sys_tables: Table = Table('Production.Product', metadata, autoload_with=self.engine)
            sys_tables: Table = Table('Product', metadata, autoload_with=self.engine, schema='Production')
            print("|***********\tSys_tables\t***********|")
            print(sys_tables)
            print("|***********\tsys_tables.metadata\t***********|")
            print(sys_tables.metadata)
            print("|***********\tsys_tables.info\t***********|")
            print(sys_tables.info)
            print("|***********\tsys_tables.schema\t***********|")
            print(sys_tables.schema)
            # select all from sys_tables
            query: Query = session.query(sys_tables)
            print("|***********\tQuery\t***********|")
            print(query)
            # print("|***********\tQuery.all()\t***********|")
            # print(query.all())
            print("|***********\tQuery.first()\t***********|")
            print(query.first())
            # print("|***********\tQuery.one()\t***********|")
            # Throws Error if more than one row is returned.
            # print(query.one())
            # print("|***********\tQuery.one_or_none()\t***********|")
            # print(query.one_or_none())
            print("|***********\tQuery.scalar()\t***********|")
            print(query.scalar())
            # print("|***********\tQuery.scalar_one()\t***********|")
            # print(query.scalar_one())
            # print("|***********\tQuery.scalar_one_or_none()\t***********|")
            # print(query.scalar_one_or_none())


            #result = session.query().from_statement(text("SELECT * FROM sys.tables"))

            # Fetch the results
            # rows = result.fetchall()
            #
            # # Process the results
            # for row in rows:
            #     print(row)
            pass

        return self._execute_query(query_func)

    def query_create_table_stmt(self, table_name: str) -> Sequence[Row[Any]]:
        def query_func(session: Session):
            metadata = MetaData()
            table = Table(table_name, metadata, autoload_with=self.engine, schema='Production')

            # get create table statement
            create_table_stmt: CreateTable = CreateTable(table)
            print(create_table_stmt)
            print('Done')

        return self._execute_query(query_func)

    def query_method_2(self):
        def query_func(session):
            # Your query logic goes here
            pass

        return self._execute_query(query_func)

    def pandas_test(self):
        df = pd.read_sql_table('Person', self.engine, schema='Person', index_col='BusinessEntityID', chunksize=10)
        dfe = enumerate(df)
        print(next(dfe))
        print(next(dfe))
        print(next(dfe))


if __name__ == "__main__":
    sqlAlchemyUtil = SqlAlchemyUtil()
    # sqlAlchemyUtil.query_all_tables()
    # sqlAlchemyUtil.query_create_table_stmt('Product')
    # config = configparser.ConfigParser()
    # config_section = 'DEFAULT'
    # config.read('config.ini')
    # server = config[config_section]['server']
    # database = 'AdventureWorks2022'
    # connection_string = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
    #
    # engine = create_engine(connection_string)
    #
    # with engine.connect() as conn:
    #     result = conn.execute(text("select * FROM sys.tables"))
    #     print(result.all())
    # result = sqlAlchemyUtil.example_basic_query()
    # print(result)
    sqlAlchemyUtil.pandas_test()
