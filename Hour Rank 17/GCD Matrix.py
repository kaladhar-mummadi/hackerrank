def gcd(a , b):
    if b == 0:
        return a
    else:
        val = gcd(b , a % b)
        return val


n,m,q = input().strip().split(' ')
n,m,q = [int(n),int(m),int(q)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
gcd_arr = []
calculated_arr = [-1] * 1000001
for i in range(n):
    arr = []
    for j in range(m):
        or_val = a[i] | b[j]
        if calculated_arr[or_val] == -1:
            value = gcd(a[i],b[j])
            arr.append(value)
            calculated_arr[or_val] = value
        else:
            arr.append(calculated_arr[or_val])
    gcd_arr.append(arr)
for a0 in range(q):

    r1,c1,r2,c2 = input().strip().split(' ')
    r1,c1,r2,c2 = [int(r1),int(c1),int(r2),int(c2)]
    # your code goes here

    values= set()
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            values.add(gcd_arr[i][j])
    print(len(values))

