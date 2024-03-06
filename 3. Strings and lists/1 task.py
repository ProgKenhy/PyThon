s= "YYYYggkeeeAAABV"
res = ""
count = 1
for i in range (0, len(s)-1):
    if (s[i]==s[i+1]):
        count+=1
    else:
        res+=s[i]
        if (count!=1):
            res+=str(count)
        count=1
    if i == len(s)-2:
        res += s[i+1]
        if (count != 1):
            res += str(count)
print(res)