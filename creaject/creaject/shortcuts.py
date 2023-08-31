import click
from os import getcwd

path_option = lambda func: click.option('-p', '--path', default=getcwd())(func)