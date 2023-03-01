"""Rename files downloaded from FZtvseries"""

import os, sys, re

#def replaceFileName(oldName, newName)
path = os.getcwd()
Fnames = os.listdir(path)
prtn = "^[0-9]{2} - "

# Remove the numbers at the beginning of tracks using regex
def removeTrackNumbers():
    for name in Fnames:
        if re.match(prtn, name):
            print("Renaming file >>> " + name + " DONE!")
            os.rename(name, getReplacementString(prtn, name))


# Using regex to replace/subtitute a string patter
# pattern: the pattern to search for
# str_to_replace: the string to search for the pattern in
def getReplacementString(pattern, str_to_replace):
    return re.sub(pattern, "", str_to_replace)

removeTrackNumbers()