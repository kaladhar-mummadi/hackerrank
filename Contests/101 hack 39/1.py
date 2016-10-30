n = int(input())
nums = [int(temp) for temp in input().split(' ')]
num_map = {}
max = 1
for i in nums:
    if i in num_map:
        num_map[i] += 1
        if max < num_map[i]:
            max = num_map[i]
    else:
        num_map[i] = 1
print(n - max)