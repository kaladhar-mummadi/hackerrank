n = int(input())
for _ in range(n):
    number = int(input())
    if number < 38 or number%5 <=2:
        print(number)
    elif number%5 > 2:
        print(number+(5-(number%5)))

