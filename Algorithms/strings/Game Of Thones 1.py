str = input()
length = len(str)
char_map = {}
i = 0
even_str = True if length % 2 ==0 else False
while i < length:
    if str[i] in char_map:
        char_map[str[i]] += 1
    else:
        char_map[str[i]] = 1
    i += 1
odds = 0
even_map = False
for key in char_map:
    if not even_str == (char_map[key] % 2 == 0):
        odds += 1

if even_str == (odds == 0):
    print("YES")
else:
    print("NO")