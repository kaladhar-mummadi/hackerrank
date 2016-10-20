actual = [int(a_temp) for a_temp in input().strip().split(' ')]
expected = [int(a_temp) for a_temp in input().strip().split(' ')]
i = 2
result = 0
while i >= 0:
    result = actual[i] - expected[i]
    if result != 0:
        break
    i -= 1
if result > 0:
    if i == 2:
        result *= 10000
    elif i == 1:
        result *= 500
    else:
        result *= 15
else:
    result = 0
print(result)
