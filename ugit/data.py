import os

def init():
    GIT_DIR = ".ugit"
    if os.path.exists(GIT_DIR):
        print("ugit repo already initialised")
    else:
        os.mkdir(GIT_DIR)
        print("ugit repo initialised")
