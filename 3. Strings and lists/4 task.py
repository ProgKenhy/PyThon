ex1 = ['abc', 'bcd', 'abc', 'abd', 'dcd', 'abc']
ex2 = ['aaa', 'bbb', 'ccc']
ex3 = ['abc', 'abc', 'abc']
array = ex1
print(array)
result = {}
for i in array:
    result[i] = result.get(i, 0) + 1
print(*list(result.values()))
