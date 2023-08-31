import click
from creaject.cli.version import version
from creaject.cli.project import new_project
from creaject.cli.template import template_cli_group

# TODO: tests add for debug as well

@click.group()
def entry_cli_group():
    pass

commands = [new_project, version, template_cli_group]

for command in commands:
    entry_cli_group.add_command(command)