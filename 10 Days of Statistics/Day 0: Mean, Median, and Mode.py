

def calculateMean(arr, n):
    sum = 0
    for num in arr:
        sum += num
    mean = sum / n
    return "%.1f" % mean

def calculateMedian(arr, n):
    arr = sorted(arr)
    mid = n // 2
    median = 0
    if n%2 == 0:
        median = (arr[mid] + arr[mid-1]) / 2
    else:
        median = arr[mid]
    return "%.1f" % median

def calculateMode(arr,n):
    numFrequency = {}
    max = 0
    mode = -1
    for num in arr:
        if num in numFrequency:
            numFrequency[num] += 1
        else:
            numFrequency[num] = 1

    for num in numFrequency:
        if max < numFrequency[num]:
            max = numFrequency[num]
            mode = num
        elif max == numFrequency[num] and mode > num:
            mode = num
    return mode
def hackerrank():
    n = int(input())
    arr = [int(temp) for temp in input().split(' ')]
    print(calculateMean(arr, n))
    print(calculateMedian(arr, n))
    print(calculateMode(arr, n))

if __name__ == '__main__':
    hackerrank()