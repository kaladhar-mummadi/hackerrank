def _hack_getTripet(n):
    if n > 11 and n%2 != 0 :
        print(-1)
        return
    val = n // 2
    i = 1
    x = 1
    while i < n:
        temp = (val // i) - i
        if temp == 0:
            break
        x = i
        y = temp
        i += 1
    a = x * x - y * y
    b = 2 * x * y
    c = x * x + y * y
    result = a * b * c
    if result > 0:
        print(result)
    else:
        print(-1)

def _euler_getTriplet():
    n = 1000
    sum = 0
    while sum < 1000:
        print(sum)
        if n > 11 and n%2 != 0 :
            print(-1)
            return
        val = n // 2
        i = 1
        x = 1
        while i < n:
            temp = (val // i) - i
            if temp == 0:
                break
            x = i
            y = temp
            i += 1
        a = x * x - y * y
        b = 2 * x * y
        c = x * x + y * y
        result = a * b * c
        sum = a + b + c
    if n == sum:
        print(result)
    else:
        print(-1)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        _hack_getTripet(N)
        #_euler_getTriplet()
