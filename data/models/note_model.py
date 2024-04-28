from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import dateutil
from kink import inject

import JsonService


@inject
@dataclass(repr=True, init=True, unsafe_hash=True)
class NoteModel:
    _author: str = field(init=True)
    content: str
    _create_date: datetime = field(init=False, default_factory=datetime.now)

    def __repr__(self):
        return f"Author: {self.author}, Date Added: {self.create_date.strftime('%B %d, %Y')}\nNote:{self.content}"

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if len(new_author) > 100:
            raise ValueError("Author name must be less than 100 characters.")
        self._author = new_author

    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, new_date):
        self._create_date = new_date

    def _load_create_date(self, new_date):
        if not isinstance(new_date, datetime):
            self._create_date = dateutil.parser.parse(new_date)
        else:
            self._create_date = new_date

    @classmethod
    def load_dict(cls, dict_data: dict) -> NoteModel:
        new_instance = cls(dict_data['author'], dict_data['content'])
        new_instance._load_create_date(dict_data['create_date'])
        return new_instance

    @classmethod
    def from_json(cls, json_data: str) -> NoteModel:
        return JsonService.json_to_class(json_data, cls)


if __name__ == "__main__":
    note_json = '{"author": "Tim H.", "content": "This is a note about something.", "create_date": "2021-01-01"}'
    note_from_json = NoteModel.from_json(note_json)
    print(note_from_json)
