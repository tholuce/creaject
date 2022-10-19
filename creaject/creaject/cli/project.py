from os import makedirs, path
import click
from rich.prompt import Prompt
from rich import print as rprint
from creaject.project import ProjectFactory
from creaject.template import choose_template
from creaject.utils import get_config


def set_variables(vars={}):
    variables = {}
    for variable_name, default_value in vars.items():
        variable_value = Prompt.ask(
            f'Enter value for variable {variable_name} ({default_value})') or default_value
        variables[variable_name] = variable_value
    return variables


@click.command('new')
@click.pass_context
def new_project(ctx):
    try:
        template_dir_path = choose_template(ctx.obj['templatePath'])
        config = get_config(template_dir_path)
        variables = config['variables'] or {}
        dest_dir_path = ctx.obj['destPath']
        if not path.exists(dest_dir_path):
            makedirs(dest_dir_path, exist_ok=True)
        if not ctx.obj['useDefaults']:
            variables.update(set_variables(variables))
        ctx.obj['variables'] = variables
        ProjectFactory(ctx, template_dir_path, dest_dir_path).create()
        print('Done.')
    except FileNotFoundError as error:
        rprint('[red]' + str(error))
        return
