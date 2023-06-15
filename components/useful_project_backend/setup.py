"""Модуль настройки setuptools.

Этот модуль играет две важные роли:
1. Через передачу аргументов в функцию setup настраивает различные аспекты
проекта.
2. Является интерфейсом командной строки для выполнения команд, относящихся к
задачам упаковки.
"""

from setuptools import find_packages, setup

setup(
    # Название проекта. При первой публикации будет зарегистрировано название,
    # которое определит:
    # 1. Как установить пакет:
    # $ pip install useful_project
    # 2. Как его найти на PyPI:
    # https://pypi.org/project/useful_project/
    name='useful_project',  # *
    # Версия согласно PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='0.0.1',  # *
    # Однострочное описание проекта
    description='Super useful project',
    # Сведения об авторе проекта.
    author='Andrey Vlasenko',
    author_email='vlasandreas@yandex-team.ru',
    # Где искать пакеты.
    packages=find_packages(where='.'),  # *
    # Поддерживаемая версия Python. Проверяются 'pip install'.
    python_requires='~=3.7',
    # Зависимости проекта, которые будут установлены pip, когда будет
    # устанавливаться проект.
    install_requires=['pydantic~=1.8.2', 'click~=7.1.2'],
    # Дополнительные группы зависимостей (например, зависимости разработки).
    # Пример установки: $ pip install useful_project[dev]
    extras_require={
        'dev': [
            'pytest~=7.2.0',
            'isort~=5.10.0',
            'yapf~=0.32.0',
            'toml~=0.10.2',
            'flake8~=6.0.0',
        ],
    },
    # Точки входа - команда `useful_project`.
    entry_points={
        'console_scripts': [
            'useful_project=useful_project.composites.cli:cli',
        ],
    },
)
