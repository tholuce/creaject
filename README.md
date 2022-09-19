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
variables in files <{{variable_name.variable_name}}>

## Libraries:

1. click - module for cli.
2. rich - https://github.com/Textualize/rich
3. PyInquirer - https://github.com/CITGuru/PyInquirer
4. pyyaml-6.0

### CLI:

    1. --version - get version for create-project
    2. --template <name of template> - generates project from specified template
    3. --export <path> - path should be specified. (with this option  --template is required)
    4. --import <path to template or url> - imports template from remote
    5. --use-defaults - if all defaults provided in config.yml then okay
    6. --path <path> - specified path to create project
    7. --inner - create project in this directory and all files in this directory. Customer already created a directory for it
    8. --name <name> - name of project or asked later (Need to add validation).
    9. --validate - validate template

### Workflow:

1. Create a project with some additional setup and teardown.
2. specify info in variables and config.yml
3. validation in config.yml
4. must be shared context among all process creation

### CICD approach:

### Useful links:

1. https://pybit.es/articles/how-to-package-and-deploy-cli-apps/
