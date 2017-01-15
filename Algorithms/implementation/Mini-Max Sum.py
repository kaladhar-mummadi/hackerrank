arr = [int(temp) for temp in input().split(" ")]

total_sum = sum(arr)
minimum = -1
maximum = -1
for i in arr:
    arbitrary_sum = total_sum - i
    if minimum == -1 or arbitrary_sum < minimum:
        minimum = arbitrary_sum
    if maximum == -1 or arbitrary_sum > maximum:
        maximum = arbitrary_sum
print(minimum, maximum)
