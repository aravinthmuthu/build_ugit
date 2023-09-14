import os
import hashlib

GIT_DIR = ".ugit"

def init():
    if os.path.exists(GIT_DIR):
        print("ugit repo already initialised")
    else:
        os.mkdir(GIT_DIR)
        os.mkdir(f'{GIT_DIR}/objects')
        print("ugit repo initialised")

def hash_object(data, type_='blob'):
    data = type_.encode() + b'\x00' + data
    object = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{object}', 'wb') as file:
        file.write(data)
    return object

def get_object(object, expected='blob'):
    with open(f'{GIT_DIR}/objects/{object}', 'rb') as file:
        obj = file.read()

    type_, data = obj.split(b'\x00')
    type_ = type_.decode()

    if expected is not None:
        assert type_==expected, f'expected {expected}, got {type_}'
    return data


