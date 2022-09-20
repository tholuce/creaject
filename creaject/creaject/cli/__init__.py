from os import getcwd
import click
from creaject.cli.version import version
from creaject.cli.project import new_project
from creaject.cli.list import list_template

#TODO: tests add for debug as well
@click.group()
@click.pass_context
@click.option('--path', '-p', default='', show_default=True)
@click.option('--use-defaults', 'use_defaults', is_flag=True, flag_value=True)
def entry_cli_group(ctx, path, use_defaults):
    obj = {
        'destPath': path or getcwd(),
        'useDefaults': use_defaults,
    }
    ctx.obj.update(obj)

commands = [new_project, list_template, version]

for command in commands: 
    entry_cli_group.add_command(command)