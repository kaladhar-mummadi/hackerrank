n,c,m = input().split(" ")
n, c, m = [int(n), int(c), int(m)]

arr =[int(temp) for temp in input().split(" ")]
arr = sorted(arr)

if m*c >= arr[-1]:
    print("Yes")
else:
    print("No")