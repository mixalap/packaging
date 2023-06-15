from useful_project.adapters.log import configure
from useful_project.adapters.storage import UsefulRepo
from useful_project.application.services import Useful


class Logger:
    configure()


class Storage:
    useful_repo = UsefulRepo()


class Application:
    useful_service = Useful(useful_repo=Storage.useful_repo)


if __name__ == '__main__':
    Application.useful_service.run()
