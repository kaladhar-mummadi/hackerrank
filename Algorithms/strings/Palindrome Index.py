t = int(input())
def checkPalindrome(str, l , r):
    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1
    return True

for _ in  range(t):
    str = input()
    i = 0
    j = len(str) - 1
    index = -1
    while i < j :
        if str[i] != str[j]:
            if str[i] == str[ j - 1] and checkPalindrome(str, i, j -1):
                index = j
                j -= 1
            elif str[i + 1] == str[j] and checkPalindrome(str, i +1, j):
                index = i
                i += 1
            else:
                break
        elif str[i] != str[j] and index !=-1:
            index = -1
            break
        else:
            i += 1
            j -= 1
    print(index)