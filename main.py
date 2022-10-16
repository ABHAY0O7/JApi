# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import click
import init
import update
import os
import convert
import json

@click.command()
@click.option('--directory', '-d', help="Directory name", default="Backend")
@click.option('--subdirectory', '-s', help="Sub-Directory name", default="Base")
@click.option('--append', '-a', default=False, is_flag=True)
@click.option('--class_name', '-c', help="Class name", default=None)
@click.option('--user_id', '-uid', help="UserId", default="id")
@click.option('--init1', '-i', default=False, is_flag=True)
@click.option('--json_path', '-j', help="Json Path", default=None)
def print_hi(directory, subdirectory, init1, append, class_name, user_id, json_path):
    if init1:
        print(f'{directory}')
        print(f'{subdirectory}')

        c1 = convert.Convertor()
        c1.path = f'{directory}/{subdirectory}'
        c1.write_to_file()

        init.Init(directory, subdirectory)
        z = update.updateFiles(directory, subdirectory)
        z.updateSettingsFile()
        z.updateURLsFile()
        os.system(f'python3 {directory}/manage.py runserver')

    elif append:
        if json_path is None:
            print(f'Provide JsonPath with --append using --json_path option')
            return
        if class_name is None:
            class_name = json_path.split('/')[-1].split('.')[0]
        print(json_path)
        print(f'{class_name}')
        print(f'{user_id}')

        c2 = convert.Convertor()
        c2.load_from_file()
        path = c2.path
        
        with open(json_path, 'r') as file:
            data = json.load(file)
            c2.ask_or_append(data, 'User')

        with open(path + '/models.py' ,'w') as f:
            f.write(c2.create_model_string())

        with open(path + '/serializers.py','w') as f:
            f.write(c2.create_serialiser_string())

        with open(path + '/views.py','w') as f:
            f.write(c2.create_views_string())
        
        with open(path + '/urls.py','w') as f:
            f.write(c2.create_urls_string())

        directory = path.split('/')[0]
        os.system(f'python3 {directory}/manage.py makemigrations')
        os.system(f'python3 {directory}/manage.py migrate')

if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
