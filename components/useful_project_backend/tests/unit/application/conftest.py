from unittest.mock import Mock

import pytest

from useful_project.application.entities import UsefulEntity
from useful_project.application.interfaces import UsefulRepo
from useful_project.application.services import Useful


@pytest.fixture(scope='function')
def useful(useful_repo):
    return Useful(useful_repo=useful_repo)


@pytest.fixture(scope='function')
def useful_repo():
    return Mock(UsefulRepo)


@pytest.fixture(scope='function')
def useful_entity():
    return UsefulEntity(id=1, useful_data='test')
