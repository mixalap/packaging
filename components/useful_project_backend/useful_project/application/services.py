import logging
from dataclasses import dataclass

from .entities import UsefulEntity
from .interfaces import UsefulRepo


@dataclass
class Useful:
    useful_repo: UsefulRepo

    def __post_init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self) -> None:
        useful_entities = self.useful_repo.get_all()
        for useful_entity in useful_entities:
            self._log_entity(useful_entity)

    def _log_entity(self, useful_entity: UsefulEntity) -> None:
        self.logger.info('got useful entity %s', str(useful_entity))
