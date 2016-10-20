N, M = input().split(" ")
N, M = [int(N), int(M)]
money_arr = [int(temp) for temp in input().split(" ")]
roads = [[False]*N for i in range(N)]
for _ in range(M):
    h1, h2 = input().split(" ")
    h1, h2 = [int(h1), int(h2)]
    roads[h1 - 1][h2 - 1] = True

def brute():
    ways = 0
    max_money = 0
    no_of_subsets = 1 << N
    for mask in range(no_of_subsets):
        ok = True
        for i in range(N):
            for j in range(N):
                if ((1 << i) & mask) and ((1 << j) & mask) and roads[i][j]:
                    ok = False
        if ok == False:
            continue
        cost = 0
        for i in range(N):
            if ((1 << i) & mask):
                cost += money_arr[i]
        if max_money < cost:
            max_money = cost
            ways = 0
        if max_money == cost:
            ways += 1
    print(max_money, ways)


if __name__ == '__main__':
    brute()

# points_map = {}
# for _ in range(M):
#     h1, h2 = input().split(" ")
#     h1, h2 = [int(h1), int(h2)]
#     if h1 in points_map:
#         points_map[h1].add(h1)
#     else:
#         points_map[h1] = {h2}
#     if h2 in points_map:
#         points_map[h2].add(h1)
#     else:
#         points_map[h2] = {h1}
# max_money = 0
# ways = 0
# ignore_houses = set()
# connected_sum_arr = []
# for i in range(M):
#     sum = 0
#     for conn in points_map[i]:
#         sum = sum + money_arr[conn - 1]
#     connected_sum_arr[i] = sum
# can_select = True
# for house in points_map:
#     if not house in ignore_houses:
#         current_money = money_arr[house - 1]
#         current_connected_money = connected_sum_arr[house - 1]
#         if current_money > current_connected_money:
#             max_money = max_money + current_money
#             ignore_houses.add(house)
#             ignore_houses.union(points_map[house])
#         elif current_money < current_connected_money:
#             ignore_houses.add(house)
#         if can_select:
#             ignore_houses = ignore_houses.union(points_map[house])
#             max_money = max_money + current_money
#
# print(max_money)
