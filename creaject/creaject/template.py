from os import listdir, path
from rich.prompt import Prompt
from rich.tree import Tree
from rich import print as rprint


def choose_template(template_path):
    template_dirs = listdir(template_path)
    tree = Tree('[green]Choose template')
    for index, templ_dir in enumerate(template_dirs):
        tree.add(f'{index + 1}. {templ_dir}')
    rprint(tree)
    print()
    template_index = int(Prompt.ask('[yellow]Enter template number'))
    return path.join(template_path, template_dirs[template_index - 1])
