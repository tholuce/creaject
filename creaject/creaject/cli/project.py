from genericpath import exists
from os import listdir, getcwd, makedirs
import click
from rich import print as rprint
from rich.tree import Tree
from rich.prompt import Prompt
from creaject.template.project import ProjectFactory
from os.path import join
from creaject.utils import get_config

def choose_template(template_path):
    template_dirs = listdir(template_path)
    tree = Tree('[green]Choose template')
    for index, templ_dir in enumerate(template_dirs):
        tree.add(f'{index + 1}. {templ_dir}')
    rprint(tree)
    print()
    template_index = int(Prompt.ask('[yellow]Enter template number'))
    return join(template_path, template_dirs[template_index - 1])

def set_variables(vars = {}):
    variables = {}
    for variable_name, default_value in vars.items():
        variable_value = Prompt.ask(f'Enter value for variable {variable_name} ({default_value})') or default_value
        variables[variable_name] = variable_value
    return variables

@click.command('new')
@click.pass_context
def new_project(ctx):
    template_dir_path = choose_template(ctx.obj['templatePath'])
    config = get_config(template_dir_path)
    variables = config['variables'] or {}
    dest_dir_path = ctx.obj['destPath']
    if not exists(dest_dir_path):
        makedirs(dest_dir_path, exist_ok=True)
    if not ctx.obj['useDefaults']:
        variables.update(set_variables(variables))
    ctx.obj['variables'] = variables
    ProjectFactory(ctx, template_dir_path, dest_dir_path).create()
    print('Done.')