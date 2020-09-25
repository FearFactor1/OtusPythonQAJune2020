import os
from os import path

# print(f'os_name: {os.name}\n')
#
# print(f'eviron: {os.environ}\n\n')
#
# print(f'current working directory {os.getcwd()}\n\n')
#
# print(f'list of files in dir: {os.listdir(os.getcwd())}')

# path_ = f'{os.getcwd()}/folder'
# os.mkdir(path_)

# print(path.join('first', 'second', 'third'))
# print(path.join('first/', 'second/', 'third/'))

# print(path.abspath(os.getcwd()))
#
# print(path.normpath(os.getcwd()))
#
# print(path.dirname(os.getcwd()))

print(path.isdir(os.getcwd()))

print(path.isfile('os_example.py'))
