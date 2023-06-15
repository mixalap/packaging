## Useful Project [Backend]
Супер полезный проект

### Стек
Click cli

### Локальное развертывание
- Развернуть виртуальное окружение Python версии 3.7 и выше, но не 4
- Обновить инструменты установки `python -m pip install --upgrade pip setuptools`
- Установить проект в режиме разработки `pip install -e .[dev]`

### Особенности запуска
- Установить переменные окружения:
    - LOGGING_LEVEL - уровень логирования
- Запустить консьюмер `python -m useful_project.composites.consumer`
- Запустить консьюмер через cli `useful_project run`
