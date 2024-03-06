s = "Y4g2ke3A3BV"
res = ""
for i in range(0, len(s)):
    if (not(s[i].isdigit())):
        res += s[i]
        temp = s[i]
    if (s[i].isdigit()):
        count=''
        while (s[i].isdigit()):
            count+=s[i]
            i+=1
        res+=temp*(int(count))
print(res)