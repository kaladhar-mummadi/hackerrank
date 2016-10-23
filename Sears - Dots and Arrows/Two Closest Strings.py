T = int(input())
for _ in range(T):
    str, K = input().split(' ')
    str = list(str)
    K = int(K)
    i = 0
    while K != 0:
        if str[i] != 'a':
            str[i] = 'b'
        else:
            str[i] = 'a'
        str.sort()
        i += 1
        K -= 1
    print(''.join(str))
