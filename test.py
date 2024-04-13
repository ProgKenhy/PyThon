import os

path = 'C:\\Users\\sasho\\Documents\\Git\\PyThon'
name = 'test.py'
print()

def obxodFile(path,name, level = 1 ):
	for i in os.listdir(path):
		if i == name:
			print('Finding =', path+'\\'+i+'\\'+name+'\n')
		if os.path.isdir(path+'\\'+i):
			for j in os.listdir(path+'\\'+i):
				if j == name:
					print('Finding =', path+'\\'+i+'\\'+name+'\n')
			obxodFile(path+'\\'+i, level+1)

obxodFile(path, name)