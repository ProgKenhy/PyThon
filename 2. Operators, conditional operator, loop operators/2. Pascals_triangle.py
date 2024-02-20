def Max_spaces(P,N):
	spaces = 0
	for i in range(len(P[N])):
		temp=P[N][i]
		while temp:
			spaces+=1
			temp//=10

	return spaces


def Number_of_spaces(P,N):
	spaces = 0
	for i in range(len(P[N])):
		temp=P[N][i]
		while temp>9:
			spaces+=1
			temp//=10
	return int(spaces/2)


N = int(input("Input natural value of N: "))
P = []


for i in range(0, N):
	row = [1] * (i+1)
	for j in range(1, i+1):
		if j != i:
			row[j] = P[i-1][j-1] + P[i-1][j]
	P.append(row)
 
maxSpaces = Max_spaces(P,N-1)
for i in range(N):
	print(" " * (maxSpaces-Number_of_spaces(P,i)-i-1), end = '')
	for j in range(i+1):
		print(P[i][j], " ", sep='', end = "")
	print()







