import os

os.chdir(os.path.dirname(os.path.realpath(__file__))) # I used it to avoid errors due to file path 
with open ('input.txt', encoding='ansi') as inputFile_, \
open('oldest.txt', 'w') as outFileForOldest_, \
open('youngest.txt', 'w') as outFileForYoungest_  :
	lines = [line.rstrip() for line in inputFile_]
	maxAge, minAge = 0, 1000
	for i in lines:
		*FullName, age = str(i).split()
		if int(age) > maxAge:
			maxAge = int(age)
			oldest = i
		if int(age) < minAge:
			minAge = int(age)
			youngest = i
	outFileForOldest_.write(oldest)
	outFileForYoungest_.write(youngest)



