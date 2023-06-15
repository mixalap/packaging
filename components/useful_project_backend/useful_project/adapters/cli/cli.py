import click


def create_cli(consumer):

    @click.group()
    def cli():
        pass

    @cli.command()
    def run():
        consumer()

    return cli
