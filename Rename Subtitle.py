#import os
""" The Script Renames content in of subtitle file downloaded from Udacity so that it will work
with VLC Player
"""

#This fuction replaces orig1 character with rep1 and orig2 with rep2 
def myreplace(line,orig1,orig2,rep1,rep2):
	new = ""
	for char in line:
		if char == orig1:
			new += rep1
		elif char == orig2:
			new += rep2
		else:
			new += char
	return new

def main():
	#os.chdir("C:\Users\Benjamin\Downloads\Compressed\GitHub Udacity\Lesson 1 Videos")
	#print os.getcwd()
	inFile = raw_input("Enter file")
	outFile = "temp.txt"
	try:
		ifile = open(inFile, 'r') #tries to open the file in read mode
		ofile = open(outFile, 'w') #tries to open the file in write mode
		for line in ifile:
			if len(line) == 24: #Checks if the length if the line is up to 24 before carry out the below operation on it.
				new = myreplace(line,'.',',',',',' --> ') #Replaces . with , and , with --> if length of line is up to 24
				ofile.write(new) #Writes the newly replaced file characters to a temp.txt file
			else:
				ofile.write(line) #Writes the original file to a temp.txt file if the lines are not upto 24
	except IOError as e:
		print e
	finally:
		ifile.close() #Closes the input/original file
		ofile.close() #Closes the output/Newly created file which is temp.txt
	copy2(outFile,inFile) #Copys and replaces the content of the output/newly created file to the input/original
	con() #Starts the whole process a new

#This fuction Replaces the original file text content with the newly created content
def copy2(arg1,arg2):
	try:
	    cpFile = open(arg1,'r')
	    rpFile = open(arg2, 'w')
	    data = cpFile.read()
	    rpFile.write(data)
	except IOError as e:
		print e
	finally:
		cpFile.close()
		rpFile.close()

#Continues the operation
def con():
	contd = raw_input("Continue? y/n \n>>>>>")
	try:
		if contd == "y":
			main()
		elif contd == "n":
			print "Goodbye Closing Script......"
		else:
			print "Not a valid answer type Y or N"
			con()
	except IOError as e:
		print e

main()
