tests = int(input())

for _ in range(tests):
    str = input()
    i = 1
    j = len(str) - 2
    funny = False
    while j > 0:
        if abs(ord(str[i]) - ord(str[i - 1])) == abs(ord(str[j]) - ord(str[j + 1])):
            funny = True
        else:
            funny = False
            break
        i += 1
        j -= 1
    if funny:
        print("Funny")
    else:
        print("Not Funny")

