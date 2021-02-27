from os import path, getcwd, listdir, mkdir, walk
import shutil
import re


TMP_FOLDER_LOCATION = '/tmp/TEMP-templaterpp/'
#TODO: make prettier
VARIABLE_REGEXP_SEARCH_PATTERN = '<{{(?P<variable_name>\w+)}}>'
VARIABLE_REGEXP_SUBSTITUE_PATTERN = lambda variable_name: '<{{' + variable_name + '}}>'

def handle_tmp():
    if path.exists(TMP_FOLDER_LOCATION):
        shutil.rmtree(TMP_FOLDER_LOCATION)
    mkdir(TMP_FOLDER_LOCATION)

def get_templates():
    template_folder_path = path.join(path.dirname(path.realpath(__file__)), 'templates')
    if not path.exists(template_folder_path):
        raise Exception('Template folder is missing in path: ' + template_folder_path)
    return template_folder_path, listdir(template_folder_path)

def select_template():
    '''
        Returns: selected template path
    '''
    template_folder_path, templates = get_templates()
    selected_template_index = None
    while not selected_template_index:
        print("Please choose template and enter index:")
        for index, template in enumerate(templates):
            print('{}. {}'.format(index + 1, template))
        selected_template_index = promt()
        if not selected_template_index:
            print("Exiting...")
            exit(1)
        if not selected_template_index.isdigit():
            selected_template_index = None
            print("Input is not digit")
            continue
        selected_template_index = int(selected_template_index)
        if selected_template_index > len(templates) or selected_template_index < 1:
            selected_template_index = None
            print("Please enter index within proposed indexes")
            continue
        
    return path.join(template_folder_path, templates[selected_template_index - 1])

def get_evaluated_variables(path):
    '''
        Returns: list of variables
    '''
    variables = set()
    for root_path, _, filesnames, in walk(path):
        for filename in filesnames:
            #FIXME: fix with path.join
            with open(root_path + '/' + filename, 'r') as template_file:
               result = re.search(VARIABLE_REGEXP_SEARCH_PATTERN ,str(template_file.read()))
               if result:
                   variables.update(result.groups())
    return variables

def evaluate_template(path, variables):
    # get_all_variables
    # replace_all_variables
    for root_path, _, filesnames, in walk(path):
        for filename in filesnames:
            #FIXME: fix with path.join
            template_file = open(root_path + '/' + filename, 'r')
            file_content = str(template_file.read())
            template_file.close()
            for variable_name, variable_value in variables.items():
                file_content = re.sub(VARIABLE_REGEXP_SUBSTITUE_PATTERN(variable_name), variable_value, file_content)
            template_file = open(root_path + '/' + filename, 'w')
            template_file.write(file_content)
            template_file.close()



def get_values_for_variables(variables):
    '''
        Returns: dictionary -> {<variable_name>: <variable_value>}
    '''
    result = {}
    print("\nStart variable inserting part")
    for variable_name in variables:
        result[variable_name] = promt("Please enter value for variable <{}>: ".format(variable_name))
    print("Done with variable part")
    return result

def promt(message = ""):
    try:
        return input(message)
    except KeyboardInterrupt:
        return None
 
def cleanup():
    # Method to clean all tmp and redudant files
    pass

def call_cli():
    template_path = select_template()
    name = promt("Please enter name: ")
    handle_tmp()
    tmp_path = path.join(TMP_FOLDER_LOCATION, 'tmp_' + name)
    shutil.copytree(template_path, tmp_path)
    variable_names = get_evaluated_variables(tmp_path)
    variables = get_values_for_variables(variable_names)
    evaluate_template(tmp_path, variables)
    dest_path = path.join(getcwd(), name)
    shutil.copytree(tmp_path, dest_path)


# if __name__ == '__main__':
#     call_cli()

#TODO: setup, install, tests and call as linux command, more print, progress