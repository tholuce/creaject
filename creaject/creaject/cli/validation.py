from os.path import exists, join
import click
from creaject.utils import get_config

def check_config(path):
    if not exists(path):
        raise Exception(f'Config file doesn\'t exist in {path}')
    config = get_config(path)
    required_fields = ['variables', 'isLocal', 'remote']
    for field in required_fields:
        if field not in config:
            raise Exception(f'Required field {field} has not been found.')

def check_folder_structure(path):
    required_folders = ['project_files']
    for required_folder in required_folders:
        if not exists(join(path, required_folder)):
            raise Exception(f'Required folder {required_folder} has not been found  in {path}')


@click.command('validate')
@click.argument('path')
def validate(path):
    check_config(path)
    check_folder_structure(path)