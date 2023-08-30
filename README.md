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

## Libraries

1. click - module for cli.
2. rich - https://github.com/Textualize/rich
3. PyInquirer - https://github.com/CITGuru/PyInquirer
4. pyyaml-6.0
5. Jinja2 - https://pypi.org/project/Jinja2/

### CLI

    1. version - get version for create-project
    2. new - generates project from specified template
    3. template
       1. init - creates new template
       2. list - list of templates
       3. export <template name or empty> (To which directory I should export?)
       4. import <local path to template dir or a git url> - imports template from remote or local dir (where I should import?)
       5. validate <path> - validate template folder specified path to create project or inner in folder.

### CLI use cases
1. creaject new - create new project from template (specified path to create project or inner in folder.)
2. creaject template list
3. creaject template import  <--path or default(current working directory)> 
4. creaject template export <--path  default(current working directory)>
5. creaject template validate  <--path  default(current working directory)>

### Workflow

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
