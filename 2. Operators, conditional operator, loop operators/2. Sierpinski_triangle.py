def Max_spaces(P, N):
    spaces = 0
    for i in range(len(P[N])):
        spaces += 1
    return spaces


def Number_of_spaces(P, N):
    spaces = 0
    for i in range(len(P[N])):
        spaces+=1
    return int(spaces)

def degree(N):
    m = 1
    while m <= N:
        if m == N:
            break
        else:
            m = m * 2
    return m



N = int(input("Input natural value of N: "))
m=degree(N)
if(m>N): N=m//2
elif N>=2: N=m
else: exit(-5)
print(N)
P = []

for i in range(0, N):
    row = [1] * (i + 1)
    for j in range(1, i + 1):
        if j != i:
            row[j] = P[i - 1][j - 1] + P[i - 1][j]
    P.append(row)

maxSpaces = Max_spaces(P, N - 1)
for i in range(N):
    print(" " * (maxSpaces - Number_of_spaces(P, i)), end='')
    for j in range(i + 1):
        if (P[i][j]%2==1):
            print('*', " ", sep='', end="")
        else:
            print(' ', " ", sep='', end="")
    print()
