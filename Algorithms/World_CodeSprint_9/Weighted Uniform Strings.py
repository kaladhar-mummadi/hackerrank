s = input().strip()
n = int(input().strip())
arr = [-1] * 26
i = 0
prev = s[0]
uniform_len = 1
for i in s[1:]:
    if prev == i:
        uniform_len += 1
    else:
        if arr[ord(prev)-97] < uniform_len:
            arr[ord(prev)-97] = uniform_len
        uniform_len = 1
        prev = i
if arr[ord(prev)-97] < uniform_len:
            arr[ord(prev)-97] = uniform_len
for a0 in range(n):
    x = int(input().strip())
    i = 1
    for i in range(1,27):
        if x%i == 0 and (i*arr[i-1] >= x):
            print("Yes")
            break
    else:
        print("No")