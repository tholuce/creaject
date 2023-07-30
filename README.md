# Name: Creaject
## Status: Under Development

## Description
> creaject creates project from templates and apply inserted variables.

### Template structure
- templates/
  - config.yml
  - project_files/

### Libraries
1. click - module for cli.
2. rich - https://github.com/Textualize/rich
3. PyInquirer - https://github.com/CITGuru/PyInquirer
4. pyyaml-6.0
5. Jinja2 - https://pypi.org/project/Jinja2/

### CLI
1. version - get version for creaject
2. new - generates project from specified template
3. template
   1. list - list of templates
   2. export <template name or empty>
   3. import <path to imported template directory> - imports template from remote or local dir 
5. validate <path> - validate template folder

### Workflow
1. Create a project with some additional setup and teardown.
2. specify info in variables and config.yml
3. validation in config.yml
4. must be shared context among all process creation

### CICD approach

### Useful links
1. https://pybit.es/articles/how-to-package-and-deploy-cli-apps/

### TODO list
2. Add tests.
3. Upgrade templates commands.
