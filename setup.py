from setuptools import setup, find_packages

setup(name='app-creator', 
    version='1.0',
    description='App-creator from templates',
    author='VV',
    packages=find_packages(exclude=['tests.*', 'tests']),
    python_requires='>=3.8'
        )