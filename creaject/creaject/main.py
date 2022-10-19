from creaject.cli import entry_cli_group
from os.path import dirname, join


def get_app_path():
    return dirname(__file__)


def get_template_path():
    return join(get_app_path(), '..', 'templates')


def app():
    obj = {
        'appPath': get_app_path(),
        'templatePath': get_template_path()
    }
    entry_cli_group(obj=obj)


if __name__ == '__main__':
    app()
