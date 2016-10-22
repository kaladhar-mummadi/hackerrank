"""
https://www.hackerrank.com/challenges/mars-exploration
"""
def calcChange(str):
    i = 0
    res = 0
    strLen = len(str)
    while i < 3:
        j = i
        while j < strLen:
            if (i == 0 or i == 2) and str[j] != 'S':
                res += 1
            elif i == 1 and str[j] != 'O':
                res += 1
            j += 3
        i += 1
    return res

if __name__ == '__main__':
    str = input()
    print(calcChange(str))