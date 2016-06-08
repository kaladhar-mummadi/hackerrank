import math
s = input().strip()
length = len(s)
sqrt_length = math.sqrt(length)
rows = int(sqrt_length)
columns = rows + 1 if (sqrt_length - int(sqrt_length)) != 0 else rows

result = ""
for i in range(columns):
    index = i
    for j in range(rows):
        if index < length:
            result += s[index]
        index += columns
    if index < length:
        result += s[index]
    result += " "
print(result.strip())