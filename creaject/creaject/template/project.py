from os import walk, makedirs
from os.path import join, relpath
from jinja2 import Template

class ProjectFactory:
    def __init__(self, ctx, template_path, dest_path) -> None:
        self._context = ctx
        self._variables = ctx.obj['variables'] or {}
        self._template_path = template_path
        self._dest_path = dest_path

    def create(self):
        project_files = join(self._template_path, 'project_files')
        for root_path, _, filesnames, in walk(project_files):
            for filename in filesnames:
                absolute_templ_path = join(root_path, filename)
                dest_path_dir = join(self._dest_path, relpath(project_files, root_path))
                makedirs(dest_path_dir, exist_ok = True)
                absolute_dest_path = join(dest_path_dir, filename)
                self._handle_template(absolute_templ_path, absolute_dest_path)

    def _handle_template(self, template_file_path, dest_file_path):
        with open(template_file_path, 'r', encoding='utf-8') as templ_file:
            template = Template(templ_file.read())
            with open(dest_file_path, 'w', encoding='utf-8') as dest_file:
                dest_file.write(template.render(self._variables))
        