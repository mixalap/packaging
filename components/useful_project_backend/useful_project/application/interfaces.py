from abc import ABC, abstractmethod
from typing import List

from .entities import UsefulEntity


class UsefulRepo(ABC):

    @abstractmethod
    def get_all(self) -> List[UsefulEntity]:
        ...
