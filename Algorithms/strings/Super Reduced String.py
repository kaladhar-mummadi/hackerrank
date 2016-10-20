str = input()
result = [str[0]]
length = 1
for i in str[1:]:
    last_char = ''
    if length > 0:
        last_char = result[-1]
    if last_char == i:
        result.pop()
        length -= 1
    else:
        result.append(i)
        length += 1
if len(result) == 0:
    print("Empty String")
else:
    print(''.join(result))