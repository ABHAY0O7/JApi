# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool
# windows, actions, and settings.

import json
import os

import click
from check import Checks

import convert
import initialize
import update
from util import print_colored


@click.command()
@click.option('--directory', '-d', help="Backend name", default="backend")
@click.option('--sub_directory', '-s',
              help="Base name", default="base")
@click.option('--append', '-a', default=False, is_flag=True)
@click.option('--class_name', '-c', help="Class name", default=None)
@click.option('--user_id', '-uid', help="UserId", default="id")
@click.option('--init', '-i', default=False, is_flag=True)
@click.option('--json_path', '-j', help="Json Path", default=None)
def jApi(
        directory,
        sub_directory,
        init,
        append,
        class_name,
        user_id,
        json_path):
    
    # Initialising the shell scripts to create a demo django backend
    if init:

        print_colored('Starting Initialization', 'header', 'b')
        
        # Storing the flags inside init_data.json file for future use 
        print_colored('Storing flags as FIELDS inside initData.json', 'blue')
        c1 = convert.Convertor()
        c1.path = f'{directory}/{sub_directory}'
        c1.write_to_file()
        print_colored('Stored successfully', 'green')

        # Invoking the shell scripts to generate a boiler django backend
        print_colored('Running automated shellscripts (initialize.sh)', 'blue')
        initialize.InitializeShellScript(directory, sub_directory)
        print_colored('Created database Successfully!', 'green', 'b')

        # Updating files
        z = update.updateFiles(directory, sub_directory)
        z.updateSettingsFile()
        z.updateURLsFile()
        print_colored('Successfully completed files update!', 'green')

        print_colored('Running Server', 'green', 'b')
        os.system(f'python3 {directory}/manage.py runserver')

    elif append:
        # Providing json path is must
        if json_path is None:
            print_colored(f'Error! - Provide JsonPath with --append using --json_path option', 'fail')
            return

        # If not provided file name, then setting it to json-file name
        if class_name is None:
            class_name = json_path.split('/')[-1].split('.')[0]
            print_colored(f'Warning! - Default class name is {class_name}', 'warning')

        print_colored('Starting json checks', 'header', 'b')
        json_checks = Checks(json_path)

        # Check JSON file existence
        if json_checks.check_file_exists() == False:
            print_colored(f'Error! with path \'{json_path}\'. Please provide a valid path to json!', 'fail')
            return
        print_colored('Passed File exist check', 'green')
        
        # Check validity of JSON data format
        try:
            json_checks.load_json()
        except BaseException:
            print_colored(f'Error loading the JSON file. JSON data Format is wrong in \'{json_path}\' file', 'fail')
            return
        print_colored('Passed json load check', 'green')
            
        # Check validity of JSON data keys format
        if json_checks.check_keys() == False:
            print(f'Error! - Please provide a valid key in json file', 'fail')
            return
        print_colored('Passed json data key format check', 'green')

        # Check validity of JSON data values format
        if json_checks.check_values() == False:
            print(f'Error! - Please provide a valid value type in json file', 'fail')
            return
        print_colored('Passed json data value format check', 'green')
        print_colored('Passed all json checks successfully!', 'green', 'b')

        # Fetching stored flag fields
        print_colored('Accessing stored flags from initData.json', 'blue')
        c2 = convert.Convertor()
        c2.load_from_file()
        path = c2.path
        print_colored('Accessed successfully', 'green')

        # TODO id feature
        with open(json_path, 'r') as file:
            data = json.load(file)
            c2.ask_or_append(data, class_name)

        # Writing backend as demanded in JSON by user
        print_colored('Starting writing backend', 'header', 'b')
        with open(path + '/models.py', 'w') as f:
            f.write(c2.create_model_string())
        print_colored('Written successfully in models.py', 'green')

        with open(path + '/serializers.py', 'w') as f:
            f.write(c2.create_serialiser_string())
        print_colored('Written successfully in serializers.py', 'green')

        with open(path + '/views.py', 'w') as f:
            f.write(c2.create_views_string())
        print_colored('Written successfully in views.py', 'green')

        with open(path + '/urls.py', 'w') as f:
            f.write(c2.create_urls_string())
        print_colored('Written successfully in urls.py', 'green')

        print_colored('Backend written successfully to all the files', 'green', 'b')

        backend_name = path.split('/')[0]
        print_colored(f'Starting migrations', 'blue')
        os.system(f'python3 {backend_name}/manage.py makemigrations')
        os.system(f'python3 {backend_name}/manage.py migrate')
        print_colored(f'Migration Successful!', 'green', 'b')


if __name__ == '__main__':
    jApi()

