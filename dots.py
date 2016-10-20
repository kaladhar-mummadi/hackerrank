
def pattern(num):
    i = 0
    str = ""
    while i < num:
        j = 0
        while j < num:
            if (i%2 == 0 and j <= i) or (j%2 ==0 and i < j):
                str += "* "
            elif j == 0 or j == num - 1 or i == 0 or i == num - 1:
                str += "* "
            else:
                str += "  "
            j += 1
        str += "\n"
        i += 1
    print(str)


if __name__ == '__main__':
    #Take n as input
    n = int(input())
    initial_value = 3
    while n > 0 :
        pattern(initial_value)
        initial_value += 2
        n -= 1