T = int(input())
for _ in range(T):
    str = input()
    str = list(str)
    i = 0
    res = 0
    openBracket = False
    openBracketList = []
    temp = 0
    lastLength = 0
    while i < len(str):
        if str[i] == '(':

            openBracketList.append(i)
            start = i
        elif len(openBracketList) > 1 and str[i] == ')':
            presentPop = openBracketList.pop()
            temp = i - presentPop + 1
            if lastLength != 0 and  temp > lastLength:
                res += temp
            lastLength = temp
        elif len(openBracketList) == 1:
            temp = 0
            lastLength = 0
            res = res + i - openBracketList.pop() + 1
        i += 1
    # if len(openBracketList) != 0:
    #     res += temp
    print(res)