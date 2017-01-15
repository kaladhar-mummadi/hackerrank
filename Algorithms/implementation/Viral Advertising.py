n = int(input())

to_start = 5
people = 0
for _ in range(n):
    who_shares = int(to_start/2)
    people += who_shares
    to_start = int(to_start/2) * 3
print(people)