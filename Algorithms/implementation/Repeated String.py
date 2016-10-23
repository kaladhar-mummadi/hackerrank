"""
https://www.hackerrank.com/challenges/repeated-string

example:
aba
10

comments explained are based on this example
"""
def calcNumberOfa(str, n):
    initialCount = str.count('a') # number of a's in aba -> 2
    strLen = len(str)   # len is 3
    quo = n // strLen   #10 // 3 -> 3
    rem = n % strLen    # 10%3 -> 1
    res = quo * initialCount    # 3 letter string is repeated 3 times totall, so 2 a's in each 3 letter totall 6 a's
    res += str[0:rem].count('a')    # and then there is one letter left that is remainder which contains 1 a
    return res
if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())
    print(calcNumberOfa(s, n))