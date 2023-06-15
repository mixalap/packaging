import pytest

from useful_project.adapters.storage import UsefulRepo
from useful_project.application.entities import UsefulEntity


@pytest.fixture(scope='function')
def useful_repo():
    return UsefulRepo()


@pytest.fixture(scope='function')
def useful_entity1():
    return UsefulEntity(id=1, useful_data='abc')


@pytest.fixture(scope='function')
def useful_entity2():
    return UsefulEntity(id=2, useful_data='xyz')
