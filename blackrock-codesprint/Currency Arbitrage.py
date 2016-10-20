tests = int(input())
total_dollars = 100000
for _ in range(tests):
    usd, eur, gbp = [float(temp) for temp in input().split(" ")]
    final = (((total_dollars / usd) / eur) / gbp)

    profit = final - total_dollars
    if profit > 0 :
        print(int(profit))
    else:
        print("0")