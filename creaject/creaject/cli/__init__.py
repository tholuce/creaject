import click
from creaject.cli.version import version

@click.group()
def entry_cli_group():
    pass

entry_cli_group.add_command(version)