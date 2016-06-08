testcases = int(input().strip())

for _ in range(testcases):
    length = int(input().strip())
    line = [int(temp) for temp in input().strip().split()]
    i = 0
    number_of_bribes = 0
    no_solution = False
    swaped = False
    while i <= length:
        j = 0
        bribes = 0
        while j < length - 1:
            if line[j] > line[j + 1]:
                bribes += 1
                temp = line[j]
                line[j] = line[j + 1]
                line[j + 1] = temp
                swaped = True
            else:
                if bribes <= 2:
                    number_of_bribes += bribes if bribes >= 0 else 0
                else:
                    no_solution = True
                    break
                bribes = 0
            j += 1
        if bribes <= 2 and no_solution != True:
            number_of_bribes += bribes
        else:
            no_solution = True
            break
        if swaped:
            swaped = False
        else:
            break
        length -= 1
        #i += 1
    if no_solution:
        print("Too chaotic")
    else:
        print(number_of_bribes)