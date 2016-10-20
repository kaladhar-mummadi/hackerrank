str = input()
str_length = len(str)

char_map = {}

for i in range(ord('a'), ord('z') + 1):
    char_map[chr(i)] = 0

for i in range(str_length):
    char_map[str[i]] += 1

can_arr = {}

for i in char_map:
    if not char_map[i] in can_arr and char_map[i] > 0:
        can_arr[char_map[i]] = 1
    elif char_map[i] in can_arr:
        can_arr[char_map[i]] += 1

if len(can_arr) > 2:
    print("NO")
else:
    for i in can_arr:
        if can_arr[i] == 1:
            print("YES")
            break
    else:
        if len(can_arr) == 1:
            print("YES")
        else:
            print("NO")