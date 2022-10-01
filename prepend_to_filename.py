import os

# Get the current working directory
path = os.getcwd()
FileNames = os.listdir(path)
for fileName in FileNames:
    if ".srt" in fileName:
        os.rename(fileName, fileName.replace(fileName, f"Eat.the.Rich.The.GameStop.Saga.S01E03.WEBRip.x265-ION265_{fileName}"))
