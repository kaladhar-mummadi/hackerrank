t = int(input())

for a0 in range(t):
    n, c, m = [int(a_temp) for a_temp in input().strip().split(' ')]
    chocolates = int(n / c)
    getToEat = leftOutWrappers = chocolates
    # chocolates = int(chocolates / m)
    while leftOutWrappers >= m:
        newlyEaten = int(leftOutWrappers / m)
        getToEat += newlyEaten
        leftOutWrappers = int(leftOutWrappers % m)
        leftOutWrappers += newlyEaten
    print(getToEat)
