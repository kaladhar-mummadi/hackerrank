n = int(input())
t = [int(a_temp) for a_temp in input().strip().split(' ')]
t.sort()
valueToSubtract = i = 0
j = i + 1

while i < n and j < n:
    print(n - i)
    while (t[i] - valueToSubtract) == (t[j] - valueToSubtract):
        j += 1
    valueToSubtract += (t[i] - valueToSubtract)
    i = j
    j += 1
print(n - i)
