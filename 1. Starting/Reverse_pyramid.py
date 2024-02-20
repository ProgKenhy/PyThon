print("Задание 2.3*")

def numberOfSpaces(place_number, temp):
	spaces=0
	for i in range (place_number, 1, -1):
		spaces_temp=(temp-int(str('9'*(i-1))))
		temp=temp-spaces_temp
		spaces+=spaces_temp*(i-1)
	return spaces

def place_of_number(temp):
	place_number=0
	while temp:
		place_number+=1
		temp//=10
	return place_number

	
n = int(input("Input natural value of n: "))
max_spaces=numberOfSpaces(place_of_number(n), n)
for i in range(n):
	temp=n-i
	result=""
	while temp>1:
		result+=str(temp)
		temp-=1
	while temp<n-i+1:
		result+=str(temp)
		temp+=1
	number_of_spaces=max_spaces-numberOfSpaces(place_of_number(n-i), n-i)+i
	print(number_of_spaces*" ", result, sep="")