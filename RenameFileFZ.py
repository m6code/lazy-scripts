"""Rename files downloaded from FZtvseries"""

import os, sys

#def replaceFileName(oldName, newName)
path = os.getcwd()
Fnames = os.listdir(path)

for fileName in Fnames:
    # if fileName.__contains__('_'):
    # 	print("Renaming file")
    # 	os.rename(fileName, fileName.replace("_"," "))
    # else:
    # 	print("No file renamed")

    # OR
    # Use the this method

    if '_' in fileName:
        print("Renaming file >>> " + fileName + "   DONE!")
        os.rename(fileName, fileName.replace("_"," "))

    elif ' high (fzmovies.net)' in fileName:
        print("Renaming file >>> " + fileName +"    DONE!")
        os.rename(fileName, fileName.replace(" high (fzmovies.net)", ""))
    else:
        print(fileName +"   NOT RENAMED!")
