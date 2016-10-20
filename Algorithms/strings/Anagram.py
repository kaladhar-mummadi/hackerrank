tests = int(input())

for _ in range(tests):
    str = input()
    length = len(str)
    result = 0
    if length == 1 or length % 2 != 0:
        print(-1)
    else:
        s1map = {}
        s2map = {}
        for i in range(ord('a'), ord('z') + 1):
            s1map[i] = 0
            s2map[i] = 0
        i = 0
        j = length - 1

        while i < j :
            s1map[ord(str[i])] += 1
            s2map[ord(str[j])] += 1
            i += 1
            j -= 1
        for i in range(ord('a'), ord('z') + 1):
            diff = s2map[i] - s1map[i]
            if diff > 0 :
                result += diff
        print(result)