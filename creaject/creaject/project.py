from os import walk, makedirs
from os import path
from jinja2 import Template


class ProjectFactory:
    def __init__(self, project_variables, template_path, dest_path) -> None:
        self._variables = project_variables or {}
        self._template_path = template_path
        self._dest_path = dest_path

    def create(self):
        '''
            Creates structure from template
        '''
        project_files_path = path.join(self._template_path, 'project_files')
        for root_path, _, filesnames, in walk(project_files_path):
            print(root_path)
            for filename in filesnames:
                absolute_templ_path = path.join(root_path, filename)
                dest_path_dir = path.join(
                    self._dest_path, path.relpath(root_path, project_files_path))
                makedirs(dest_path_dir, exist_ok=True)
                absolute_dest_path = path.join(dest_path_dir, filename)
                self._handle_template(absolute_templ_path, absolute_dest_path)
    
    def _handle_template(self, template_file_path, dest_file_path):
        with open(template_file_path, 'r', encoding='utf-8') as templ_file:
            template = Template(templ_file.read())
            with open(dest_file_path, 'w', encoding='utf-8') as dest_file:
                dest_file.write(template.render(self._variables))
