from setuptools import setup, find_packages
from sys import platform

setup(
    name = 'creaject', 
    version = '0.1',
    description = 'Create project from template',
    author = 'VV',
    packages = find_packages(exclude=['tests.*', 'tests']),
    python_requires = '>=3.8',
    entry_points = {
        'console_scripts': ['creaject=creaject.main:app']
    },
    scripts = [
        'install_templates.ps1' if platform == 'win32' else 'install_templates.sh'
    ]
)