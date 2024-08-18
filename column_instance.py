from dataclasses import dataclass

from sql_column_type import SQLColumnType


@dataclass
class ColumnInstance:
    alias: str
    table: str
    sql_column_type: SQLColumnType
    is_nullable: bool
    condition: str | None
    description: str
