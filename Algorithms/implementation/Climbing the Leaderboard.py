n = int(input())
scores = [int(temp) for temp in input().split(" ")]
m = int(input())
alice_levels = [int(temp) for temp in input().split(" ")]
ranks = [0]*n
i = 1
ranks[0] = 1
while i < n:
    if scores[i] == scores[i-1]:
        ranks[i] = ranks[i-1]
    elif scores[i] < scores[i-1]:
        ranks[i] = ranks[i-1] +1
    i += 1
i = n -1
for level in alice_levels:
    while i>=0 and scores[i] <= level:
        i -= 1
    if i == -1:
        print(1)
    else:
        print(ranks[i]+1)
