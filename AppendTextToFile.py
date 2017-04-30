# This scripts adds character to a filename
# Keeping the original name
# Just Appending additional text to the end

import os

# Get the current working directory
path = os.getcwd()
FileNames = os.listdir(path)
for fileName in FileNames:
    os.rename(fileName, fileName + ".mp4" )
