# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import click
import init
import update
import os

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


if __name__ == '__main__':
    outpur = print_hi()
    print(outpur)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
