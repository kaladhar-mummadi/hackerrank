n = int(input())
seq = [int(temp) for temp in input().split(' ')]
arr = []
one_sub = False
for i in range(n-1):
    if seq[i] > seq[i+1]:
        arr.append(i)
    elif len(arr) > 1:
        arr.append(i)
        break
    elif len(arr) !=0:
        break
more_than_one = False
if len(arr) == 0:
    print("yes")
else:
    for i in range(arr[-1]+1, n-1):
        if seq[i] > seq[i+1]:
            arr.append(i+1)
            more_than_one = True
            break
    else:
        if seq[-2] > seq[-1]:
            arr.append(n-1)

    if len(arr) == 2:
        print("yes")
        print("swap "+ str(arr[0]+1) +" " + str(arr[1]+1))
    elif more_than_one == False and len(arr) > 2:
        print("yes")
        print("reverse "+ str(arr[0]+1) +" " + str(arr[-1]+1))
    else:
        print("no")