s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
result_apple = 0
result_orange = 0
for i in apple:
    if s <= (a + i) <= t:
        result_apple += 1
for i in orange:
    if s <= (b + i) <= t:
        result_orange += 1
print(result_apple)
print(result_orange)
