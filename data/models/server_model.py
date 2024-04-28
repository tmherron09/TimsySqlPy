from dataclasses import dataclass, field
from typing import List

from data.models.note_model import NoteModel


@dataclass
class ServerModel:
    _name: str
    _environment: str
    notes: List[NoteModel] = field(default_factory=list)

    @property
    def name(self):
        return f"[{self._name}]"

    @property
    def environment(self):
        return f"[{self._environment}]"

    @classmethod
    def load_dict(cls, dict_data: dict):
        return cls(dict_data['_name'], dict_data['_environment'], dict_data['notes'])


server = ServerModel("localhost", "dev")
print(server.name)  # [localhost]



