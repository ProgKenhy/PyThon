a = set(map(int, input().split()))
b = set(map(int, input().split()))
if len(a.intersection(b)) == len(a) and len(a) != len(b):
    print("True")
else:
    print("False")