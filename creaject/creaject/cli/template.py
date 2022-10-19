from os import listdir, path
from shutil import copytree
from turtle import color
import click
from rich import print as rprint
from rich.tree import Tree
from creaject.template import choose_template
from creaject.errors import TemplateValidationError
from creaject.validators import validators_list


@click.command('validate')
@click.pass_context
def validate_template(ctx):
    try:
        templ_validation_path = ctx.obj['destPath']
        rprint(f"Validating template under path: {templ_validation_path}")
        for validator in validators_list:
            validator(templ_validation_path)
        rprint('Template validation completed: Everything is okay')
    except (TemplateValidationError, FileNotFoundError) as exception:
        rprint('[red]' + str(exception))


@click.command('list')
@click.pass_context
def list_template(ctx):
    tree = Tree("Templates")
    # TODO: check if templates dir exists
    dir_templates = listdir(ctx.obj['templatePath'])
    for index, template_name in enumerate(dir_templates):
        tree.add(f'{index + 1}. {template_name}')
    rprint(tree)
    print()


@click.command('import')
@click.pass_context
def import_template(ctx):
    current_folder = ctx.obj['destPath']
    template_name = path.basename(current_folder)
    template_root_location = ctx.obj['templatePath']
    copytree(current_folder, path.join(template_root_location, template_name))


@click.command('export')
@click.argument('name', required=False)
@click.pass_context
def export_template(ctx, name: str = ''):
    templates_root_folder_path = ctx.obj['templatePath']
    template_folder_path = choose_template(
        templates_root_folder_path) if not name else path.join(ctx.obj['templatePath'], name)
    try:
        copytree(template_folder_path, ctx.obj['destPath'], dirs_exist_ok=True)
        rprint('[green]Template exported successfully')
    except Exception as e:
        rprint(e)


@ click.group('template')
def template_cli_group():
    pass


template_cli_group.commands = {"import": import_template,
                               "export": export_template, "list": list_template, "validate": validate_template}
