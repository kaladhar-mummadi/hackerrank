str = input()
alpha_set = set()
pangram = False
length = len(str)
if length >= 26:
    i = 0
    while i < length:
        chr = str[i]
        if chr <= 'Z' and chr >= 'A':
            chr = chr.lower()
        if chr >= 'a' and chr <= 'z':
            alpha_set.add(chr)
        if i >= 26 and len(alpha_set) == 26:
            pangram = True
            break
        i += 1
if pangram:
    print("pangram")
else:
    print("not pangram")