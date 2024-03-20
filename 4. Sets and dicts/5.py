from collections import defaultdict
n = int(input())
dict_ = defaultdict(list)
for i in range(n):
    client, product, value = map(str, input().split())
    dict_[client].append(product + " " + value)
for i in list(dict_.keys()):
    print("ID = ", i, ":")
    for j in dict_[i]:
        print(j)


