# import os

# path = 'C:\\Users\\sasho\\Documents\\Git\\PyThon'
# name = 'test.py'
# print()

# def obxodFile(path,name, level = 1 ):
# 	for i in os.listdir(path):
# 		if i == name:
# 			print('Finding =', path+'\\'+i+'\\'+name+'\n')
# 		if os.path.isdir(path+'\\'+i):
# 			for j in os.listdir(path+'\\'+i):
# 				if j == name:
# 					print('Finding =', path+'\\'+i+'\\'+name+'\n')
# 			obxodFile(path+'\\'+i, level+1)

# obxodFile(path, name)

# def fact(n):
# 	pr=1
# 	a=[]
# 	for i in range(1,n+1):
# 		pr*=i
# 		yield pr

# for i in fact(10000000):
# 	temp = i
# print(temp)

# s = (map(int, input().split()))
# print(s)



# print(any((0,0, '1')))


# name = 'Сергей'
# mid_name = 'Иванов'
# balance = 32.33

# text = """ Уважаемый {0} {1} ваш Баланс лицевого счёта {2} """.format(name, mid_name, balance)
# print(text)

#Замыкания
# def average_numbers():
# 	numbers = []

# 	def inner(number):
# 		numbers.append(number)
# 		print(numbers)
# 		return sum(numbers)/len(numbers)
# 	return inner
# r = average_numbers()
# print(r(100))
# print(r(20))



# from time import perf_counter

# def timer():
# 	start = perf_counter()

# 	def inner():

# 		return perf_counter() - start
# 	return inner

# q = timer()
# print(q())
# q = timer()
# print(q())


# def add(a,b):
# 	return a+b

# def counter(func):
# 	count = 0
# 	def inner(*args, **kwargs):
# 		nonlocal count
# 		count+=1
# 		print(f"Функция {func.__name__} вызывалась {count} раз")
# 		return func(*args, **kwargs)
# 	return inner

# q = counter(add)
# print(q(10,2))
# print(q(10,22))


#decorator
# def header(func):
# 	def inner(*args, **kwargs):
# 		print('<h1>')
# 		func(*args, **kwargs)
# 		print('</h1>')
# 	return inner

# def table(func):
# 	def inner(*args, **kwargs):
# 		print('<table>')
# 		func(*args, **kwargs)
# 		print('</table>')
# 	return inner

# @header #say = header(say)
# @table #say = header(table(say))
# def say(name, surname, age):
# 	print('Hello', name, surname, age)

# # say = table(header(say))
# say('Vasya', 'Ivanov', 15)


#V2
# from functools import wraps


# def table(func):

# 	@wraps(func)
# 	def inner(*args, **kwargs):
# 		print('<table>')
# 		func(*args, **kwargs)
# 		print('</table>')
# 	return inner

# def say():
# 	print('hello world')

# def sqr(x):
# 	"""
# 	Функция возводит в квадрат x
# 	:param x:
# 	:return:
# 	"""
# 	print(x**2)

# print(sqr(2))
# sqr = table(sqr)

# print(sqr(4))
# print(help(sqr))


import math