from enum import Enum
from typing import List


class JoinType(Enum):
    INNER_JOIN = "INNER JOIN"
    LEFT_JOIN = "LEFT JOIN"
    RIGHT_JOIN = "RIGHT JOIN"
    FULL_OUTER_JOIN = "FULL OUTER JOIN"


class TableRelationship:
    def __init__(self, database_a: str | None, database_b: str | None, schema_a: str = 'dbo', schema_b: str = 'dbo', *,
                 table_a: str, table_b: str, column_a: str, column_b: str, alias_a: str = None, alias_b: str = None):
        self.table_a = {"database": database_a, "schema": schema_a, "table": table_a, "column": column_a,
                        "alias": alias_a}
        self.table_b = {"database": database_b, "schema": schema_b, "table": table_b, "column": column_b,
                        "alias": alias_b}

    @classmethod
    def from_dict(cls, table_a: dict, table_b: dict):
        return cls(table_a.get('database', None), table_b.get('database', None), table_a.get('schema', 'dbo'),
                   table_b.get('schema', 'dbo'), table_a=table_a['table'], table_b=table_b['table'],
                   column_a=table_a['column'], column_b=table_b['column'], alias_a=table_a.get('alias', None),
                   alias_b=table_b.get('alias', None))


class on_clause:
    def __init__(self, schema: str | None, table: str, column: str, columns: List = None, alias: str = None):
        self.schema = schema if schema else 'dbo'
        self.table = table
        self.column = add_square_bracket(column)
        self.columns = add_square_brackets(columns)
        self.alias = add_square_bracket(alias)
        self.has_on_join_multiple_columns = len(self.columns) > 1

    def join_to(self) -> str:
        if self.alias:
            return f'{self.schema}.{self.table} AS {self.alias}'
        return f'{self.schema}.{self.table}'

    @classmethod
    def from_dict(cls, table: dict):
        return cls(table.get('schema', 'dbo'), table['table'], table['column'], table.get('alias', None))


class JoinTable:
    def __init__(self, join_type: JoinType, on_source: on_clause,
                 on_target: on_clause):
        self.join_type = join_type
        self.on_source = on_source
        self.on_target = on_target

    @classmethod
    def from_direct(cls, join_type: JoinType, source_schema: str | None, source_table: str, source_column: str,
                    target_schema: str | None, target_table: str, target_column: str, source_alias: str = None,
                    target_alias: str = None):
        on_source = on_clause(source_schema, source_table, source_column, source_alias)
        on_target = on_clause(target_schema, target_table, target_column, target_alias)
        return cls(join_type, on_source, on_target)

    @classmethod
    def from_table_relationship(cls, join_type: JoinType, table_relationship: TableRelationship):
        return cls(join_type, on_clause.from_dict(table_relationship.table_a), on_clause.from_dict(table_relationship.table_b))

    def format_from(self, schema: str, table: str, alias: str = None) -> str:
        if alias:
            return f'FROM {schema}.{table} AS {alias}'
        return f'FROM {schema}.{table}'

    def format_join(self) -> str:
        return f'\n\t{self.join_type} {self.on_target.join_to()}\n\t\tON {self.on_source.column} = {self.on_target.column}'


sql = """
SELECT 
    {columns}
FROM dbo.User
"""


def add_square_brackets(columns: list) -> list:
    if not columns:
        return columns
    return [f'[{column.strip()}]' if not (column.startswith('[') and column.endswith(']'))
            else column for column in columns]


def add_square_bracket(item: str | None) -> str:
    if not item:
        return item
    item = item.strip()
    return item if not (item.startswith('[') and item.endswith(']')) else f'[{item}]'


def format_from(schema: str, table: str, alias: str = None) -> str:
    if alias:
        return f'FROM {schema}.{table} AS {alias}'
    return f'FROM {schema}.{table}'


def format_join(join_type: str, source_table: dict, target_table: dict, on_source: dict, on_target: dict) -> str:
    source = format_from(source_table['schema'], source_table.get('table', 'dbo'), source_table.get('alias', None))
    target = format_from(target_table['schema'], target_table.get('table', 'dbo'), target_table.get('alias', None))
    on_source = add_square_bracket(on_source['column']) if on_source else None
    on_target = add_square_bracket(on_target['column']) if on_target else None
    return f'{join_type} {source} JOIN {target} ON {on_source} = {on_target}'


def format_columns(sql: str, columns: list) -> str:
    columns_str = '\n\t,'.join(columns)
    return sql.format(columns=columns_str)


formated_sql = format_columns(sql, ['id', 'name', 'email'])
print(formated_sql)
