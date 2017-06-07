import os

def LoadImages(argv):
    directory = os.walk(argv)
    for dirpath, dirnames, filenames in directory:
        pass
