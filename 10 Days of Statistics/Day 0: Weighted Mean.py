def calculateWeightedMean(arr,weights, n):
    sum = 0
    totalWeigth = 0
    i = 0
    while i < n:
        sum += (arr[i]*weights[i])
        totalWeigth += weights[i]

        i += 1
    mean = sum / totalWeigth
    return "%.1f" % mean

def hackerrank():
    n = int(input())
    arr = [int(temp) for temp in input().split(' ')]
    weights = [int(temp) for temp in input().split(' ')]
    print(calculateWeightedMean(arr, weights, n))

if __name__ == '__main__':
    hackerrank()