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

def hash_object(data):
    object =  hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{object}', 'wb') as file:
        file.write(data)
    return object

def get_object(object):
    with open(f'{GIT_DIR}/objects/{object}', 'rb') as file:
        return file.read()

