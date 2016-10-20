import math
N = int(input())
repeated_map = {}
numbers = [int(temp) for temp in input().split(" ")]
sorted = True
for i in range(N):
    num = numbers[i]
    if num in repeated_map:
        repeated_map[num] += 1
    else:
        repeated_map[num] = 1
    if sorted and i < N - 1 and numbers[i] > numbers[i + 1]:
        sorted = False
repeated_product = 1
for i in repeated_map:
    repeated =  repeated_map[i]
    if repeated > 0:
        repeated_product *= math.factorial(repeated)
fact_value = math.factorial(N) // repeated_product
if sorted or fact_value == 1:
    print("0.000000")
else:
    print("{0:.6f}".format(fact_value))