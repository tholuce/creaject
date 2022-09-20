# Name: creaject

## Description:

> create-project creates project from templates.

## Architecture

create-project:

- templates(folder):
  - config.yml
  - before(folder with multiple scripts)
  - after(folder with multiple scripts)
  - project_files(folder):
  -

before/after entry point

context to pass data among scripts and data about where path
For Templates use Jinja2. 

## Libraries:

1. click - module for cli.
2. rich - https://github.com/Textualize/rich
3. PyInquirer - https://github.com/CITGuru/PyInquirer
4. pyyaml-6.0
5. Jinja2 - https://pypi.org/project/Jinja2/

### CLI:

    1. version - get version for create-project
    2. list - list of templates
    3. new - generates project from specified template
    4. export <path> - path should be specified.
    5. import <path to template dir or url> - imports template from remote or local dir
    6. --use-defaults - if all defaults provided in config.yml then okay
    7. --path <path> - specified path to create project or inner in folder.
    8.  validate - validate template

### Workflow:

1. Create a project with some additional setup and teardown.
2. specify info in variables and config.yml
3. validation in config.yml
4. must be shared context among all process creation

### CICD approach:

### Useful links:

1. https://pybit.es/articles/how-to-package-and-deploy-cli-apps/

### Features:
1. before and after scripts.
