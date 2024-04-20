from enum import Enum
from typing import List, TypeVar

T = TypeVar('T')

class OrderByEnum(Enum):
    ASC = "ASC"
    DESC = "DESC"

class SqlWhereClause:
    def __init__(self, column: str, value: T, operator: str = "="):
        self.column = column
        self._value = value
        self.operator = operator
        self._type = type(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, self._type):
            raise TypeError(f"Expected value of type {self._type}, got {type(new_value)}")
        self._value = new_value

    def __str__(self):
        if isinstance(self._value, str):
            return f"{self.column} {self.operator} '{self.value}'"
        else:
            return f"{self.column} {self.operator} {self.value}"

    def __repr__(self):
        return str(self)



class SqlStatement:
    def __init__(self, source_identifier: str, database_name:str, schema_name: str, table_name: str, columns: str | List[str] = None):
        if source_identifier is None and (database_name is None or schema_name is None or table_name is None):
            raise ValueError("Required source_identifier or all of the following: database_name, schema_name, "
                             "and table_name must be provided")

        if columns is None:
            self.columns =["*"]
        else:
            self.columns = [columns] if isinstance(columns, str) else columns
        # if isinstance(columns, str):
        #     self.columns = [columns]
        # else:
        #     self.columns = columns
        self._source_identifier: str = None
        self.database_name: str = database_name
        self.schema_name: str = schema_name
        self.table_name: str = table_name
        self.where_clause: List[SqlWhereClause] = None
        self.group_by: List[str] = None
        self.order_by: List[str] = None
        self.order_direction: OrderByEnum = OrderByEnum.ASC
        self.top: int = None

    def __str__(self):
        return self.build_sql()

    def add_where_clause(self, column: str, value: T, operator: str = "="):
        if self.where_clause is None:
            self.where_clause = []
        self.where_clause.append(SqlWhereClause(column, value, operator))

    def add_group_by(self, column: str | List[str]) -> None:
        if self.group_by is None:
            self.group_by = []
        if isinstance(column, str):
            self.group_by.append(column)
        else:
            self.group_by.extend(column)


    def add_order_by(self, column: str | List[str]) -> None:
        if self.order_by is None:
            self.order_by = []
        if isinstance(column, str):
            self.order_by.append(column)
        else:
            self.order_by.extend(column)


    def set_ordered_direction(self, direction: OrderByEnum):
        self.order_direction = direction

    def set_top(self, top: int):
        self.top = top

    def build_sql(self) -> str:
        sql = "SELECT "
        if self.top:
            sql += f"TOP({self.top})"
        sql += "\n\t" + '\n\t,'.join(self.columns) + "\nFROM " + self.table_name
        if self.where_clause:
            if isinstance(self.where_clause, list):
                self.where_clause = '\n\tAND '.join([ str(condition) for condition in self.where_clause])
            sql += "\n\tWHERE " + self.where_clause
        if self.group_by:
            if isinstance(self.group_by, list):
                self.group_by = ', '.join(self.group_by)
            sql += "\n\tGROUP BY " + self.group_by
        if self.order_by:
            if isinstance(self.order_by, list):
                self.order_by = ', '.join(self.order_by)
            sql += "\n\tORDER BY " + f"{self.order_by} {self.order_direction.value}"
        return sql



def build_simple_sql_select_statement(columns: List[str], table_name: str, where_clause: str | List[str] = None, group_by: str | List[str] = None, order_by: str = None, order_direction: OrderByEnum = OrderByEnum.ASC, top: int = None) -> str:
    """
    Build a simple SQL SELECT statement with the given columns, table name, where clause, order by, and limit.
    """
    sql = "SELECT "
    if top:
        sql += f"TOP({top})"
    sql += "\n\t" + '\n\t,'.join(columns) + "\nFROM " + table_name
    if where_clause:
        if isinstance(where_clause, list):
            where_clause = '\n\tAND '.join(where_clause)
        sql += "\n\tWHERE " + where_clause
    if group_by:
        if isinstance(group_by, list):
            group_by = ', '.join(group_by)
        sql += "\n\tGROUP BY " + group_by
    if order_by:
        if isinstance(order_by, list):
            order_by = ', '.join(order_by)
        sql += "\n\tORDER BY " + f"{order_by} {order_direction.value}"

    return sql

sql_output = build_simple_sql_select_statement(columns=["column1", "column2"], table_name="table1", where_clause=["column1 = 'value1'", "column2 = 'value2'"], group_by=["column1", "column2"], order_by=["column1", "column2"], order_direction= OrderByEnum.DESC, top=10)

print(sql_output)

sql_statement = SqlStatement(source_identifier=None, database_name="database1", schema_name="dbo", table_name="table1", columns=["column1", "column2", "column3"])
sql_statement.add_order_by(["column1", "column2"])
test_c: char = 'c'
sql_statement.add_where_clause("column2", operator= ">", value= 'c')
sql_statement.add_group_by(["column1", "column2"])
sql_statement.set_ordered_direction(OrderByEnum.DESC)
sql_statement.set_top(1000)
sql_statement.add_order_by("column3")

print("Printing the Class:\n\n")
print(sql_statement)