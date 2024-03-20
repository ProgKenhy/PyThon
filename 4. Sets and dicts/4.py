string_ = list(input().split())
dict_ = {}
result = ""
for i in string_:
    dict_[i] = dict_.get(i, 0) + 1
    result += str(dict_.get(i)-1) + " "
print(result)