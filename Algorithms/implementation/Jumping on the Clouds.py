def calcSteps(arr, n):
    i = 0
    steps = 0
    while i != n - 1:
        if i < n - 2 and arr[i + 2] == '0':
            steps += 1
            i += 2
        else:
            steps += 1
            i += 1
    return steps
if __name__ == '__main__':
    n = int(input())
    str = input().strip().split(' ')
    print(calcSteps(str, n))