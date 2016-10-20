n = int(input())
grid = []
for i in range(n):
    temp = list(input().strip())
    grid.append(temp)
print("".join(grid[0]))
i = 1
while i < n - 1:
    j = 1
    result = grid[i][j - 1]
    while j < n - 1:
        currentValue = grid[i][j]
        if (grid[i][j - 1] < currentValue and
                    grid[i - 1][j] < currentValue and
                    grid[i][j + 1] < currentValue and
                    grid[i + 1][j] < currentValue):
            result += 'X'
        else:
            result += currentValue
        j += 1
    result += grid[i][j]
    print(result)
    i += 1
if i == n - 1:
    print("".join(grid[n - 1]))
