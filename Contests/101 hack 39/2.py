n, k = input().split(' ')
n, k =[int(n), int(k)]
num_map = {}
towers = [int(temp) for temp in input().split(' ')]
times = [0] * 100000
switched_on = 0
total_on = 0
i = 0
while i < n:
    if towers[i] == 1:
        j = i
        t = 0
        while t < k:
            times[j] += 1
            t += 1
            j += 1
        j = i - 1
        t = 1
        while t < k:
            times[j] += 1
            t += 1
            j -= 1
    i += 1
towers_sorted = sorted(times, reverse= True)[0:n]
towers_sorted = sorted(towers_sorted)
max = 1
num = 2
if towers_sorted[0] == 0:
    print(-1)
else:
    for i in towers_sorted:
        if i in num_map:
            num_map[i] += 1
        else:
            num_map[i] = 1
        if max < num_map[i] and i < num:
            max = num_map[i]
            num = i
    print(num)
# while i < n:
#     if towers[i] == 0:
#         total_on += 2*k -1
#         if ((i + k - 1) < n and towers[i + k - 1] == 1) or ((i - k + 1) >= 0 and towers[i -k +1] == 1) :
#             j = 0
#             t = n -1 if (i + k -1) >= n else (i + k -1)
#             while j < k and t < n:
#                 bool[t] = True
#                 j += 1
#                 t += 1
#             j = 0
#             t = 0 if (i - k + 1) < 0 else (i - k + 1)
#             while j < k and t >= 0:
#                 bool[t] = True
#                 j += 1
#                 t -= 1
#         switched_on += 1
#         i = i + k -1
#     i += 1
# i = 0
# while i < n and total_on != n:
#     if towers[i] == 1 and bool[i] == False:
#         if ((i + k - 1) < n and towers[i + k - 1] == 1) or ((i - k + 1) >= 0 and towers[i -k +1] == 1) :
#             j = 0
#             t = n - 1 if (i + k -1) >= n else (i + k -1)
#             while j < k and t < n:
#                 total_on += 0 if bool[t] else 1
#                 bool[t] = True
#                 j += 1
#                 t += 1
#             j = 0
#             t = 0 if (i - k + 1) < 0 else (i - k + 1)
#             while j < k and t >= 0:
#                 total_on += 0 if bool[t] else 1
#                 bool[t] = True
#                 j += 1
#                 t -= 1
#         switched_on += 1
#         i = i + k -1
#     i += 1

#print(switched_on)

