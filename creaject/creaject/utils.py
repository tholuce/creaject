import os
from os.path import join as pathjoin, exists
from sys import platform
import yaml
from typing import Literal, Dict
from creaject.constants import TEMPLATE_CACHE_FILE_NAME, TEMPLATE_FOLDER_NAME, APP_NAME

def get_config(path: Literal) -> Dict:
    config_file_path = pathjoin(path, 'config.yml')
    if not exists(config_file_path):
        raise FileNotFoundError(
            f'Config file doesn\'t exist in template: {config_file_path}')
    return yaml.safe_load(open(config_file_path, 'r').read())

def get_root_folder_path() -> Literal:
        match platform:
            case 'linux' | 'linux2':
                return '/opt/creaject'
            case 'win32':
                return pathjoin(os.getenv('APPDATA'), APP_NAME)
  
def get_template_path() -> Literal:
    return pathjoin(get_root_folder_path(), TEMPLATE_FOLDER_NAME)

def get_template_cache_file_path() -> Literal:
    return pathjoin(get_root_folder_path(), TEMPLATE_CACHE_FILE_NAME)