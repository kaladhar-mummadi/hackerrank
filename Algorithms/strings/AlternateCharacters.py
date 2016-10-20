tests = int(input().strip())

for _ in range(tests):
    str = input()
    prev = str[0]
    number_of_deletions = 0
    i = 1
    while i < len(str):
        if prev == str[i]:
            number_of_deletions += 1
        else:
            prev = str[i]
        i += 1
    print(number_of_deletions)