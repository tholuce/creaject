from os.path import exists, join
from creaject.errors import TemplateValidationError


def validate_folder_structure(path):
    required_folders = ['project_files']
    for required_folder in required_folders:
        if not exists(join(path, required_folder)):
            raise TemplateValidationError(
                f'Required folder {required_folder} has not been found  in {path}')
