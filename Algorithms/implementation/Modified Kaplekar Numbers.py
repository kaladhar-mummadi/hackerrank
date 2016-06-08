p = int(input().strip())
q = int(input().strip())

result_arr = []
atleast_one_kaplekar_number = False
for n in range(p , q + 1):
    square_val = n * n
    square_val_arr = []
    #counts number of digits in current number
    temp = n
    d = 0
    while temp != 0 :
        temp = int(temp/10)
        d += 1
    dividend = pow(10, d)
    r = square_val % dividend
    l = int(square_val / dividend)
    total_sum = l + r
    if total_sum == n:
        result_arr.append(n)
        atleast_one_kaplekar_number = True

if atleast_one_kaplekar_number == False:
    print("INVALID RANGE")
else:
    print(*result_arr)