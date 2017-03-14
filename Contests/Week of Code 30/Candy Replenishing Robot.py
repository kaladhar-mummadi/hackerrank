n, t = input().split(" ")
[n,t] = [int(n), int(t)]
candies = [int(temp) for temp in input().split(" ")]
count = 0
temp_n = n
for i in candies[:-1]:
    remaining = temp_n - i
    temp_n = remaining
    if remaining < 5:
        count += (n - remaining)
        temp_n += (n-remaining)
print(count)