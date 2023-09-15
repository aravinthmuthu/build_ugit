from . import data
import os

def write_tree (directory='.'):
    items = os.listdir(directory)
    for item in items:
        full_path = os.path.join(directory,item)
        if not is_ignored(full_path):
            if os.path.isfile(full_path):
                with open(full_path, 'rb') as file:
                    obj = file.read()
                    print(data.hash_object(obj), full_path)
            elif os.path.isdir(full_path):
                write_tree(full_path)

def is_ignored(path):
    # TO-DO add regex support
    ignore_list = ['.ugit','.git','.gitignore', "__pycache__","ugit.egg-info"]
    ignore = False
    for l in ignore_list:
        if l in path.split('/'):
            ignore = True
    return ignore
