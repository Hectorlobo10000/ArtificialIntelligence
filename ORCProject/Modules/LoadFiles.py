import os
import fnmatch

def LoadImages(argv):
    directory = os.walk(argv)
    key = 0
    dictionaryForFullPath = {}
    dictionaryFileName = {}
    fullDictionary = {}
    for dirPath, dirNames, fileNames in directory:
        for name in fileNames:
            fullPath = dirPath + name
            if fnmatch.fnmatch(fullPath, '*.jpg') or fnmatch.fnmatch(fullPath, '*.png') or fnmatch.fnmatch(fullPath, '*.jpeg') or fnmatch.fnmatch(fullPath, '*.bmp'):
                key = key + 1
                dictionaryForFullPath[key] = fullPath
                dictionaryFileName[key] = name
    fullDictionary[1] = dictionaryForFullPath
    fullDictionary[2] = dictionaryFileName
    return fullDictionary
