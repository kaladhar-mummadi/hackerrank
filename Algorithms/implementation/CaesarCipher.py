strLen = int(input())
str = list(input())
k = int(input())
for i in range(strLen):
    asciiValue = ord(str[i])
    if 65 <= asciiValue <= 90:
        str[i] = chr(((asciiValue - 65 + k) % 26) + 65)
    elif 97 <= asciiValue <= 122:
        str[i] = chr(((asciiValue - 97 + k) % 26) + 97)
print("".join(str))
