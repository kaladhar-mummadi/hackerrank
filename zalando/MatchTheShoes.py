import operator
k, m, n = [int(temp) for temp in input().strip().split(' ')]
orders = []
orders_repeated_number = {}
for i in range(n):
    orderId = int(input())
    orders.append(orderId)
    if orderId in orders_repeated_number:
        orders_repeated_number[orderId] += 1
    else:
        orders_repeated_number[orderId] = 0
sorted_orders_repeated_number = sorted(orders_repeated_number.items(), key = operator.itemgetter(1), reverse = True)
i = 0
while i < k:
    if i < k - 1 and sorted_orders_repeated_number[i][1] == sorted_orders_repeated_number[i + 1][1]:
        if sorted_orders_repeated_number[i][0] < sorted_orders_repeated_number[i + 1][0]:
            print(sorted_orders_repeated_number[i][0])
            i += 1
            if i < k:
                print(sorted_orders_repeated_number[i][0])
        else:
            print(sorted_orders_repeated_number[i + 1][0])
            i += 1
            if i < k:
                print(sorted_orders_repeated_number[i - 1][0])
        i += 1
    else:
        print(sorted_orders_repeated_number[i][0])
        i += 1