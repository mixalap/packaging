from dataclasses import dataclass
from typing import List

from useful_project.application import interfaces
from useful_project.application.entities import UsefulEntity


@dataclass
class UsefulRepo(interfaces.UsefulRepo):

    def get_all(self) -> List[UsefulEntity]:
        return [
            UsefulEntity(id=1, useful_data='abc'),
            UsefulEntity(id=2, useful_data='xyz'),
        ]
