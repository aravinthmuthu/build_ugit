import argparse
from . import data

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

    commit_parser = subparser.add_parser('commit')
    commit_parser.add_argument("-m","--message")
    commit_parser.set_defaults(func=commit)

    add_parser = subparser.add_parser('add')
    add_parser.add_argument("files", nargs='*')
    add_parser.set_defaults(func=add)
    
    args = parser.parse_args()
    return args
    
def init(args):
    data.init()

def hash_object(args):
    with open(args.file, 'rb') as file:
        print(data.hash_object(file.read()))

def add(args):
    print("files ready to be added to staging:",args.files)

def commit(args):
    print("ready to commit")
    print("commit message :", args.message)

if __name__ == "__main__":
    main()