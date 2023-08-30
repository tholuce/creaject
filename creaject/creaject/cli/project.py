from os import makedirs
from os.path import exists as path_exists
import click
from rich.prompt import Prompt
from rich import print as rprint
from creaject.project import ProjectFactory
from creaject.shortcuts import path_option
from creaject.utils import get_config
from creaject.template import choose_template

@click.command('new')
@path_option
def new_project(path):
    '''
        Create new project from template under path variable
        :param path: destination path
    '''
    try:
        template_path = choose_template()
        config = get_config(template_path)
        variables = config.get('variables') or []
        if not path_exists(path):
            makedirs(path, exist_ok=True)
        project_variables = __set_project_variables(variables)
        ProjectFactory(project_variables, template_path, path).create()
        rprint(f'[green]Done creating project in {path}')
    except FileNotFoundError as error:
        rprint('[red]' + str(error))
        return


def __set_project_variables(variable_list=[]):
    variables = {}
    for variable_name in variable_list:
        variable_value = Prompt.ask(
            f'Enter value for variable called [yellow]{variable_name}')
        variables[variable_name] = variable_value
    return variables
        