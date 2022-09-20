from posixpath import abspath
from os import listdir
import click
from rich import print as rprint 
from rich.tree import Tree


@click.command('list')
@click.pass_context
def list_template(ctx):
    tree = Tree("Templates")
    print('name'+ ctx.obj['name'])
    #TODO: check if templates dir exists
    dir_templates = listdir(ctx.obj['templatePath'])
    for index, template_name in enumerate(dir_templates):
        tree.add(f'{index + 1}. {template_name}')
    rprint(tree)
    print()