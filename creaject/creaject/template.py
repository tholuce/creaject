from os import listdir, path
from rich.prompt import Prompt
from rich.tree import Tree
from rich import print as rprint
from creaject.errors import TemplateValidationError
from creaject.validators import validators_list


def choose_template(template_path):
    template_dirs = listdir(template_path)
    if not any(template_dirs):
        raise FileNotFoundError(
            'You dont have any templates saved. Please import some using command `creaject template import`')
    tree = Tree('[green]Choose template')
    for index, templ_dir in enumerate(template_dirs):
        tree.add(f'{index + 1}. {templ_dir}')
    rprint(tree)
    print()
    template_index = int(Prompt.ask(
        f'[yellow]Enter template number(1-{len(template_dirs)}) '))
    return path.join(template_path, template_dirs[template_index - 1])


def is_template_folder_valid(templ_validation_folder):
    rprint(f"Validating template under path: {templ_validation_folder}")
    try:
        for validator in validators_list:
            validator(templ_validation_folder)
            rprint('Template validation completed: Everything is okay')
            return True
    except (TemplateValidationError, FileNotFoundError) as exception:
        rprint('[red]' + str(exception))
        return False
