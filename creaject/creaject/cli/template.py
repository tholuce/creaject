from os import listdir, path
from shutil import copytree
import click
from rich import print as rprint
from rich.tree import Tree
from creaject.template import choose_template, is_template_folder_valid


@click.command('validate')
@click.pass_context
def validate_template(ctx):
    templ_validation_path = ctx.obj['destPath']
    is_template_folder_valid(templ_validation_path)


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
    templ_src_folder = ctx.obj['destPath']
    if not is_template_folder_valid(templ_src_folder):
        return
    template_name = path.basename(templ_src_folder)
    template_root_location = ctx.obj['templatePath']
    copytree(templ_src_folder, path.join(
        template_root_location, template_name))


@click.command('export')
@click.argument('name', required=False)
@click.pass_context
def export_template(ctx, name: str = ''):
    try:
        templates_root_folder_path = ctx.obj['templatePath']
        template_folder_path = choose_template(
            templates_root_folder_path) if not name else path.join(ctx.obj['templatePath'], name)
        copytree(template_folder_path, ctx.obj['destPath'], dirs_exist_ok=True)
        rprint('[green]Template exported successfully')
    except FileNotFoundError as error:
        rprint('[red]' + str(error))


@ click.group('template')
def template_cli_group():
    pass


template_cli_group.commands = {"import": import_template,
                               "export": export_template, "list": list_template, "validate": validate_template}
