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

        elif os.path.isdir(full_path):
            type_ = 'tree'
            oid = write_tree(full_path)
        
        print(oid, full_path) 
        entries.append((item, oid, type_))
    
    tree = ''
    for entry in entries:
        item, oid, type_ = entry
        tree = tree + f'{type_} {oid} {item}\n'

    return data.hash_object(tree.encode(), 'tree')


def get_tree_entries(tree_oid):
    tree_data = data.get_object(tree_oid, expected='tree').decode().splitlines()
    entries = []
    for line in tree_data:
        entries.append(line.split(" "))

    return entries


def read_tree(tree_oid, path='.'):

    if not os.path.exists(path):
        os.mkdir(path)

    entries = get_tree_entries(tree_oid)
    for entry in entries:
        type_, oid, name = entry
        assert '/' not in name
        assert name not in ['.','..']

        if type_ == 'blob':
            with open(os.path.join(path,name), 'wb') as file:
                print(oid, os.path.join(path,name))
                file.write(data.get_object(oid, expected='blob'))
        elif type_ == 'tree':
            read_tree(oid, path=os.path.join(path,name))
        else:
            assert False, f'Unknown entry type {type_}'



def is_ignored(path):
    # TO-DO add regex support
    ignore_list = ['.ugit','.git','.gitignore', "__pycache__","ugit.egg-info"]
    ignore = False
    for l in ignore_list:
        if l in path.split('/'):
            ignore = True
    return ignore
