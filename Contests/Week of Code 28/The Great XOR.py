import math
q = int(input())
for _ in range(q):
    x = int(input())
    no_of_bits = 0
    temp = x
    while (temp):
        no_of_bits += 1
        temp >>= 1
    no_of_bits -= 1
    last_two_power = int(math.pow(2, no_of_bits))
    diff = x - last_two_power
    print(last_two_power - diff - 1)