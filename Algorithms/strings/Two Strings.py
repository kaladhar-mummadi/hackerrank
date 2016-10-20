t = int(input())

for _ in range(t):
    str1 = set(input())
    str2 = set(input())
    common = str1.intersection(str2)
    if len(common) != 0:
        print("YES")
    else:
        print("NO")