import os

os.chdir(os.path.dirname(os.path.realpath(__file__))) # I used it to avoid errors due to file path 
with open ('input.txt') as inputFile_, open('output.txt', 'w') as outFile_ :
	lines = [int(line.rstrip()) for line in inputFile_]
	lines.sort()
	for i in lines:
		outFile_.write(str(i)+'\n')


