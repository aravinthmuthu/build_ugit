from . import data
import os

def write_tree (directory='.'):
    items = os.listdir(directory)
    for item in items:
        full_path = os.path.join(directory,item)
        if os.path.isfile(full_path):
            print(full_path)
        elif os.path.isdir(full_path):
            write_tree(full_path)
