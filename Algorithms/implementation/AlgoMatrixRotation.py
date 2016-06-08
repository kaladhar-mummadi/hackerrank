m, n, r = [int(temp) for temp in input().strip().split(" ")]

matrix = []
for _ in range(0,m):
    row = input().strip().split(" ")
    matrix.append(row)


top = 0
bottom = m - 1
left = 0
right = n - 1

number_of_rows = m
number_of_columns = n
while top < bottom and left < right:
    mod_r = r % ((number_of_rows * 2) + 2 * (number_of_columns - 2))
    number_of_rows -= 2
    number_of_columns -= 2
    for test in range(0, mod_r):
        prev = matrix[top][left + 1]
        for i in range(top, bottom):
            #left
            curr = matrix[i][left]
            matrix[i][left] = prev
            prev = curr
        #bottom
        for i in range(left, right):
            curr = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = curr
        #right
        for i in range(bottom, top, -1):
            curr = matrix[i][right]
            matrix[i][right] = prev
            prev = curr
        #top
        for i in range(right, left, -1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr
    top += 1
    left += 1
    bottom -= 1
    right -= 1
for i in range(0, m):
    print(" ".join(matrix[i]))