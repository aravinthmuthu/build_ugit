import argparse
from . import data
from . import base
import sys

def main():
    args = parse_args()
    # print(args)
    if hasattr(args, 'func'):   
        args.func(args)


def parse_args():
    parser = argparse.ArgumentParser()

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command',help="command subparser")

    init_parser = subparser.add_parser('init')
    init_parser.set_defaults(func=init)

    hash_object_parser = subparser.add_parser('hash-object')
    hash_object_parser.add_argument('file')
    hash_object_parser.set_defaults(func=hash_object)

    cat_file_parser = subparser.add_parser('cat-file')
    cat_file_parser.add_argument('object')
    cat_file_parser.set_defaults(func=cat_file)

    write_tree_parser = subparser.add_parser('write-tree')
    write_tree_parser.set_defaults(func=write_tree)

    read_tree_parser = subparser.add_parser('read-tree')
    read_tree_parser.set_defaults(func=read_tree)
    read_tree_parser.add_argument('tree')
    
    args = parser.parse_args()
    return args
    
def init(args):
    data.init()

def hash_object(args):
    with open(args.file, 'rb') as file:
        print(data.hash_object(file.read()), 'test')   # can also pass in type_ parameter

def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object, expected=None))   # can pass a second argument called expected

def write_tree(args):
    print(base.write_tree(),'.')

def read_tree(args):
    base.read_tree(args.tree)

if __name__ == "__main__":
    main()