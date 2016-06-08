testcases = int(input().strip())
for _ in range(testcases):
    n = int(input().strip())
    a = [int(temp) for temp in input().strip().split(' ')]
    b = []
    inversion_sum = 0
    for i in range(n):
        j = i + 1
        inversion = 0
        while j < n:
            if a[j] < a[i]:
                inversion += 1
            j += 1
        inversion_sum += inversion

    if inversion_sum % 2 == 0 :
        print("YES")
    else:
        print("NO")