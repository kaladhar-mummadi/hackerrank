str_len = int(input())
str = input()
min_repeated = str_len / 4
i = 0
count = {'A': 0,
         'C': 0,
         'T': 0,
         'G': 0}
extra_count = {'A': 0,
               'C': 0,
               'T': 0,
               'G': 0}
while i < str_len:
    count[str[i]] += 1
    i += 1

extra_count['A'] = 0 if count['A'] <= min_repeated else count['A'] - min_repeated
extra_count['C'] = 0 if count['C'] <= min_repeated else count['C'] - min_repeated
extra_count['T'] = 0 if count['T'] <= min_repeated else count['T'] - min_repeated
extra_count['G'] = 0 if count['G'] <= min_repeated else count['G'] - min_repeated

l = 0
r = 0
max_possible_len = 0
sub_str_count = {'A': 0,
               'C': 0,
               'T': 0,
               'G': 0}
while r < str_len:
    sub_str_count[str[r]] += 1

    got_string = True
    for i in extra_count:
        if sub_str_count[i] < extra_count[i]:
            got_string = False
            break
    if got_string:
        break
    r += 1
min_len = r + 1
while True:
    sub_str_count[str[l]] -= 1
    l += 1


    got_string = True
    for i in extra_count:
        if sub_str_count[i] < extra_count[i]:
            r += 1
            sub_str_count[str[r]] += 1
            got_string = False
            break
    if got_string:
        min_len -= 1
    elif r == str_len - 1:
        break
print(min_len)