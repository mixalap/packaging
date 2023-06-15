from useful_project.adapters.cli import create_cli

from .consumer import Application

cli = create_cli(Application.useful_service.run)
