""" 
A script that ::
-- Create a sub-folder in current directory
-- Select every file with specified extension
-- Move files to created folder above
"""

import os
import shutil

source = './'
destination = './sub/'
files = os.listdir(source)

'''Create the directory '''
def createFolder(dir):
    try:
        if not os.path.exists(dir):  # Check if directory does not exist
            os.makedirs(dir) # Create the specified directory
    except OSError:
        print ('Error: Creating directory. ' +  dir)

def moveFiles():
	for file in files:
		#if ('.py' in file): # Check if file contains .srt in the name
		if (file.endswith(".srt")): # Check if the file ends with .srt
			shutil.move(file, destination) # Move file to the destination folder
		else:
			print ("No file with .srt extension")
    
# Creates a folder in the current directory called sub
createFolder('./sub/')

# Move files with specified extension to folder
moveFiles()





"""
import shutil
import os

source = '/path/to/source_folder'
dest1 = '/path/to/apple_folder'
dest2 = '/path/to/intel_folder'

files = os.listdir(source)

for f in files:
    if (f.startswith("Apple") or f.startswith("apple")):
        shutil.move(f, dest1)
    elif (f.startswith("Intel") or f.startswith("intel")):
        shutil.move(f, dest2)
"""

