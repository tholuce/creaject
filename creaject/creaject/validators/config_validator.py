from os.path import exists
from rich import print as rprint
from creaject.utils import get_config
from creaject.errors import TemplateValidationError


def validate_config(path):
    rprint('[yellow]Validating config')
    config = get_config(path) or {}
    required_fields = ('variables',)
    for field in required_fields:
        if field not in config:
            raise TemplateValidationError(
                f'Required field called: "{field}" has not been found.')
