str1 = input()
str2 = input()
length1 = len(str1)
length2 = len(str2)

str1_map = {}
str2_map = {}

for i in range(ord('a'), ord('z') + 1):
    str1_map[chr(i)] = 0
    str2_map[chr(i)] = 0
for i in range(length1):
    str1_map[str1[i]] += 1
for i in range(length2):
    str2_map[str2[i]] += 1
result = 0
for i in range(ord('a'), ord('z') + 1):
    result += abs(str1_map[chr(i)] - str2_map[chr(i)])
print(result)