import Modules.LoadFiles

def Main():
    directory = raw_input("Enter a directory: ")
    print(Modules.LoadFiles.LoadImages(directory))
Main()
