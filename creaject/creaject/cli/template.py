from os import getcwd, mkdir
from os.path import join as pathjoin
import click
from rich import print as rprint
from rich.tree import Tree
from creaject.template import is_template_folder_valid, get_template_list, import_template, export_template
from creaject.shortcuts import path_option

#TODO: add testing
@click.command('validate')
@click.option('--p', '--path')
def validate_template(path):
    is_template_folder_valid(path or getcwd())
        
@click.command('list')
def list_templates():
    tree = Tree("Templates")
    for index, template_name in enumerate(get_template_list()):
        tree.add(f'{index + 1}. {template_name}')
    rprint(tree)
    print()

@click.command('init')
@path_option # TODO: test it and change everywhere if works
def init_template(path):
    mkdir(pathjoin(path, 'project_files'))
    with open(pathjoin(path, 'config.yml'), ) as config_file:
        config_file.write('variables:')    

@click.command('import')
@click.option('--p', '--path')
def import_template(path):
   import_template(path or getcwd())

@click.command('export')
@click.option('--path')
def export_template(path):
    export_template(path)

@click.group('template')
def template_cli_group():
    pass


template_cli_group.commands = {"import": import_template,
                               "export": export_template,
                               "list": list_templates,
                               "validate": validate_template}