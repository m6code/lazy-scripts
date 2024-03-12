import os

# Get the current working directory
path = os.getcwd()
FileNames = os.listdir(path)
for fileName in FileNames:
    os.rename(fileName, fileName.replace("%20"," "))
