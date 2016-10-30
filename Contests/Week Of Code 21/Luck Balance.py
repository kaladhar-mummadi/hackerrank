N, K = input().split(" ")
N, K = [int(N), int(K)]
imp_array = []
un_imp_array = []
for _ in range(N):
    luck, imp = input().split(" ")
    luck, imp = [int(luck), int(imp)]
    if imp == 1:
        imp_array.append(luck)
    else:
        un_imp_array.append(luck)
imp_array.sort()
length = len(imp_array)
if K >= length:
    result = sum(imp_array) + sum(un_imp_array)
else:
    result = sum(imp_array[length - K:]) + sum(un_imp_array) - sum(imp_array[0:length - K])
print(result)
