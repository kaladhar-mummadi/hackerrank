testcases = int(input())
for a0 in range(testcases):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    onTimeNumberOfStudents = 0
    arr = [int(a_temp) for a_temp in input().strip().split(' ')]
    for a1 in arr:
        if a1 <= 0:
            onTimeNumberOfStudents += 1
    if onTimeNumberOfStudents >= k:
        # class not cancelled
        print("NO")
    else:
        print("YES")
