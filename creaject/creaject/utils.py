from os.path import join, exists
import yaml


def get_config(path):
    config_file_path = join(path, 'config.yml')
    if not exists(config_file_path):
        raise FileNotFoundError(
            f'Config file is not exist in template: {path}')
    return yaml.safe_load(open(config_file_path, 'r').read())
