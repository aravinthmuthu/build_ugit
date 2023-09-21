from . import data
import os

def write_tree (directory='.'):
    items = os.listdir(directory)
    entries = []
    for item in items:
        full_path = os.path.join(directory,item)
        if is_ignored(full_path):
            continue

        if os.path.isfile(full_path):
            with open(full_path, 'rb') as file:
                obj = file.read()
                type_ = 'blob'
                oid = data.hash_object(obj)
                print(oid, full_path)

        elif os.path.isdir(full_path):
            type_ = 'tree'
            oid = write_tree(full_path)
        
        entries.append((item, oid, type_))
    
    tree = ''
    for entry in entries:
        item, oid, type_ = entry
        tree = tree + f'{type_} {oid} {item}\n'

    return data.hash_object(tree.encode(), 'tree')

    

def is_ignored(path):
    # TO-DO add regex support
    ignore_list = ['.ugit','.git','.gitignore', "__pycache__","ugit.egg-info"]
    ignore = False
    for l in ignore_list:
        if l in path.split('/'):
            ignore = True
    return ignore
