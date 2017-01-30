import math
n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
split_val = int(math.sqrt(n))
box = list(map(int, input().strip().split(' ')))
#box = [temp for temp in range(1000001)]
min_arr = []
sum_arr = []

if n >= split_val:
    base = 0
    while base < n:
        min_arr.append(min(box[base:base+split_val]))
        sum_arr.append(sum(box[base:base+split_val]))
        base +=split_val
def getMin(l,r):
    if r-l < split_val:
        return min(box[l:r+1])
    first_elem = int(l/split_val)
    last_elem = int(r/split_val) - 1
    simple_min_arr = []
    if l%split_val !=0:
        first_min = min(box[l:l*(first_elem+1) + 1])
        first_elem += 1
    else:
        first_min = min_arr[first_elem]
    if r%split_val != 0:
        last_min = min(box[split_val*last_elem:r+1])
    else:
        last_min = min_arr[last_elem]
        last_elem += 1
    simple_min_arr.append(first_min)
    simple_min_arr.append(last_min)
    if first_elem != last_elem:
        simple_min_arr.append(min(min_arr[first_elem:last_elem]))
    return min(simple_min_arr)
def getSum(l,r):
    if r-l < split_val:
        return sum(box[l:r+1])
    first_elem = int(l/split_val)
    last_elem = int(r/split_val)
    if l%split_val !=0:
        first_sum = sum(box[l:l*(first_elem+1) + 1])
        first_elem += 1
    else:
        first_sum = 0
    if r%split_val !=0 :
        last_sum = sum(box[split_val*last_elem: r +1])
    else:
        last_sum = 0
        last_elem += 1
    if first_elem != last_elem:
        mid_sum = sum(sum_arr[first_elem:last_elem])
    else:
        mid_sum = 0
    return sum([first_sum, mid_sum, last_sum])
for _ in range(q):
    op = list(map(int, input().strip().split(' ')))
    if op[0] == 1:
        minimum_value = None
        for i in range(op[1],op[2]+1):
            temp = box[i]+op[3]
            box[i] = temp
            if minimum_value == None or minimum_value > temp:
                minimum_value = temp
            if i!=0 and i%(split_val) == split_val - 1:
                min_arr[int(i/split_val)] = minimum_value
                minimum_value = None
            sum_arr[int(i/split_val)] += op[3]
        if minimum_value != None:
            min_arr[int(i/split_val)] = minimum_value
    elif op[0] == 2:
        minimum_value = None
        for i in range(op[1],op[2]+1):
            temp = math.floor(box[i]/op[3])
            prev = box[i]
            box[i] = temp
            if minimum_value == None or minimum_value > temp:
                minimum_value = temp
            if i!=0 and i%(split_val) == split_val - 1:
                min_arr[int(i/split_val)] = minimum_value
                minimum_value = None
            sum_arr[int(i/split_val)] -= prev
            sum_arr[int(i/split_val)] += temp
        if minimum_value != None:
            min_arr[int(i/split_val)] = minimum_value
    elif op[0] == 3:
        print(getMin(op[1], op[2]))
    elif op[0] == 4:
        print(getSum(op[1], op[2]))

