from enum import Enum


class SQLColumnType(Enum):
    VARCHAR = "VARCHAR"
    CHAR = "CHAR"
    TEXT = "TEXT"
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    SMALLINT = "SMALLINT"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    DECIMAL = "DECIMAL"
    DATE = "DATE"
    TIME = "TIME"
    TIMESTAMP = "TIMESTAMP"
    BOOLEAN = "BOOLEAN"
    BLOB = "BLOB"
    CLOB = "CLOB"
    UUID = "UUID"
    # Column Contains VARCHAR of comma delimited values.
    CSV = "CSV"
