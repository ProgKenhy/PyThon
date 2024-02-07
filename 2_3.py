
print("Задание 2.3*")
n = int(input("Input natural value of n: "))
max_place_number=0
max_spaces=0
temp=n
while temp:
	max_place_number+=1
	temp//=10
temp=n
for i in range (max_place_number, 1, -1):
	max_spaces_temp=(temp-int(str('9'*(i-1))))
	temp=temp-max_spaces_temp
	max_spaces+=max_spaces_temp*(i-1)
for i in range(n):
	temp=n-i
	result=""
	while temp>1:
		result+=str(temp)
		temp-=1
	while temp<n-i+1:
		result+=str(temp)
		temp+=1
	temp_now_value=n-i
	place_number=0
	spaces_number=0
	while temp_now_value:
		place_number+=1
		temp_now_value//=10
	temp=n-i
	if (n-i)>9:
		spaces_res=0
	else:
		spaces_res=0
	for j in range (place_number, 1, -1):
		spaces_res_temp=(temp-int(str('9'*(j-1))))
		temp=temp-spaces_res_temp
		spaces_res+=spaces_res_temp*(j-1)
	number_of_spaces=max_spaces-spaces_res+i
	print(number_of_spaces*" ", result, sep="")