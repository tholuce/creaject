from os import path, listdir
from shutil import copytree
from rich.prompt import Prompt
from rich.tree import Tree
from rich import print as rprint
from creaject.errors import TemplateValidationError
from creaject.validators import validators_list
from creaject.utils import get_template_cache_file_path, get_template_path
from typing import AnyStr, List


def import_template(path: AnyStr):
    if not is_template_folder_valid(path):
        return
    try:
        template_name = path.basename(path)
        template_root_location = get_template_path()
        copytree(path, path.join(template_root_location, template_name))
        update_template_cache()
        rprint('[green]Template exported successfully')
    except Exception as error:
        rprint('[red]' + error)


def export_template(path: AnyStr):
    try:
        template_folder_path = choose_template()
        copytree(template_folder_path, path, dirs_exist_ok=True)
        rprint('[green]Template exported successfully')
    except FileNotFoundError as error:
        rprint('[red]' + str(error))


def get_template_list() -> List[AnyStr]:
    if not path.exists(get_template_cache_file_path()):
        update_template_cache()
    with open(get_template_cache_file_path(), 'r') as template_cache_file:
        return template_cache_file.read().splitlines()


def choose_template() -> AnyStr:
    template_list = get_template_list()
    if not any(template_list):
        raise FileNotFoundError(
            'You dont have any templates saved. Please import some using command `creaject template import`')
    tree = Tree('[green]Choose template')
    for index, template_name in enumerate(template_list):
        tree.add(f'{index + 1}. {template_name}')
    rprint(tree)
    print()
    template_index = int(Prompt.ask(
        f'[yellow]Enter template number(1-{len(template_list)}) '))
    return path.join(get_template_path(), template_list[template_index - 1])


def is_template_folder_valid(templ_validation_folder) -> bool:
    rprint(f"Validating template under path: {templ_validation_folder}")
    try:
        for validator in validators_list:
            validator(templ_validation_folder)
            rprint('Template validation completed: Everything is okay')
            return True
    except (TemplateValidationError, FileNotFoundError) as exception:
        rprint('[red]' + str(exception))
        return False


def update_template_cache():
    templates = listdir(get_template_path())
    with open(get_template_cache_file_path(), 'w') as cache_fp:
        cache_fp.write('\n'.join(templates))