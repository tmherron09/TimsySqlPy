import dataclasses
from typing import List


@dataclasses
class Proc():
    name: str
    parameters: str #TODO: Create Parameter Class.
    server: str
    database_location: str #TODO: Create Database Class.
    database_refs: List[str]
    table_list: List[str] #TODO Create Table Class.


