n = int(input())
i = 0
price_time_list = []
price_time_list_len = 0
while i < n:
    event = [int(temp) for temp in input().strip().split()]
    max_price = -1
    if event[0] == 1:
        price_time_pair= (event[1], event[2])
        price_time_list.append(price_time_pair)
        price_time_list_len += 1
    elif event[0] == 2:
        minimumTime = event[1] - 59
        j = price_time_list_len - 1
        while  price_time_list[j][1] >= minimumTime and j >= 0:
            if  price_time_list[j][1] <= event[1]:
                if max_price < price_time_list[j][0]:
                    max_price = price_time_list[j][0]
            j -= 1
        print(max_price)
    i +=1