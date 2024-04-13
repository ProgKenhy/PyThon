import os

os.chdir(os.path.dirname(os.path.realpath(__file__))) # I used it to avoid errors due to file path 
with open ('input.txt') as inputFile_:
	a = inputFile_.readline().split()
	result = 1
	for i in a:
		result *= int(i)
with open('output.txt', 'w') as outFile_:
	outFile_.write(str(result))

