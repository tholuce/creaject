from creaject.constants import VERSION
import click

@click.command()
@click.version_option(VERSION)
def version():
    print(f'version: {VERSION}')