import dataclasses
from typing import List

from sql_column_type import SQLColumnType
from column_instance import ColumnInstance

@dataclasses
class ColumnEntry():
    name: str
    sql_column_type: SQLColumnType
    column_instance: List[ColumnInstance]
    procs_using: List[Proc]






