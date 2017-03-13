n = int(input())
arr = [int(temp) for temp in input().split(" ")]
for i in range(n):
    first_p = arr.index(i+1)+1
    print(arr.index(first_p)+1)