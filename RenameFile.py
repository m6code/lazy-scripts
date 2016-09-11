import os
"""Renames files in a directory
(1)deletes the %20 appended to it
(2)replaces it with space

Usage:
python RenameFile.py
put in directory you wish to rename
Mostly works with files downloaded with opera mini
"""

# Get the current working directory
path = os.getcwd()
FileNames = os.listdir(path)

#Renames files in the working directory containing %20 with Spaces
def main():
	try:
	    for fileName in FileNames:
	        os.rename(fileName, fileName.replace(" ","%20"))
	except WindowsError as e:
		print "There are no files with the %20 character in this directory"

#Calls the main function
main()
