n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if grade < 38 or grade%5 == 0:
        print(grade)
        continue
    diff = grade%5
    if diff > 2:
        print(grade+(5-diff))
    else:
        print(grade)

