length = int(input())
ar = [int(i) for i in input().strip().split()]
left = []
right = []
equal = []
element = ar[0]
for i in range(0,length):
    if ar[i] == element:
        equal.append(ar[i])
    elif ar[i] > element:
        right.append(ar[i])
    elif ar[i] < element:
        left.append(ar[i])
print(" ".join(map(str,left + equal + right)))