import click

@click.command()
@click.option('--version', default='0.1')
def version():
    click.echo('version: 0.1')