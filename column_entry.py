from dataclasses import dataclass
from typing import List

from proc import Proc
from sql_column_type import SQLColumnType
from column_instance import ColumnInstance

@dataclass
class ColumnEntry:
    name: str
    sql_column_type: SQLColumnType
    column_instance: List[ColumnInstance]
    procs_using: List[Proc]






