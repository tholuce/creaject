# Name: Creaject
# Under Development!

## Description:

> creaject creates project from templates.

## Architecture

create-project:

- templates(folder):
  - config.yml
  - project_files(folder):

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
    2. new - generates project from specified template
    3. template
       1. list - list of templates
       2. export <template name or emty>
       3. import <path to template dir or url> - imports template from remote or local dir
    
    4. --path <path> - specified path to create project or inner in folder.
    5. validate <path> - validate template folder

### Workflow:

1. Create a project with some additional setup and teardown.
2. specify info in variables and config.yml
3. validation in config.yml
4. must be shared context among all process creation

### CICD approach:

### Useful links:

1. https://pybit.es/articles/how-to-package-and-deploy-cli-apps/

### Features:
1. before and after scripts. For example: git init.
2. Add tests.
3. Upgrade templates commands.
