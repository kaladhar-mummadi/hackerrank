S = input()
length = len(S)
freq_need_a = {}
rev_S = S[::-1]
freq_s = {}
positions = {}
next_to_use = {}

for i in range(ord('a'), ord('z') + 1):
    freq_need_a[chr(i)] = 0
    freq_s[chr(i)] = 0
    next_to_use[chr(i)] = 0
    positions[chr(i)] = []

# character distribution of s
i = 0
while i < length:
    freq_s[rev_S[i]] += 1
    positions[rev_S[i]].append(i)

    i += 1

# character distribution for A

for i in freq_s:
    count = int(freq_s[i] / 2)
    if count > 0:
        freq_need_a[i] = count

freq_seen = {}
needs = [0] * length
written = {}

for i in range(ord('a'), ord('z') + 1):
    freq_seen[chr(i)] = 0
    written[chr(i)] = 0


j = length - 1
while j >= 0:
    char = rev_S[j]
    if freq_seen[char] < freq_need_a[char]:
        needs[j] = freq_need_a[char] - freq_seen[char]
        freq_seen[char] += 1
    else:
        needs[j] = 0
    j -= 1

i = 0
initial_position = 0
result = ""
bottle_neck = 0
while i < length / 2:
    while not written[rev_S[bottle_neck]] < needs[bottle_neck]:
        bottle_neck += 1
    next_char = 'a'
    while written[next_char] == freq_need_a[next_char] or positions[next_char][next_to_use[next_char]] > bottle_neck:
        next_char = chr(ord(next_char) + 1)
    str_pos = positions[next_char][next_to_use[next_char]]
    while initial_position < str_pos:
        next_to_use[rev_S[initial_position]] += 1
        initial_position += 1
    while True:
        result += next_char
        written[next_char] += 1
        next_to_use[next_char] += 1
        if not written[next_char] < needs[str_pos]:
            break
    initial_position = str_pos + 1

    i += 1
print(result)