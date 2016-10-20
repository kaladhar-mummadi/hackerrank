n = int(input())
incremented_stocks = 0
next_10_min_stock_length = 0
prev_10_min_stock_length = 0
number_of_people_with_ratings = {}

ratings = [int(temp) for temp in input().split(" ")]
min_stocks = [int(temp) for temp in input().split(" ")]

max_stock_of_min_rating = 0
min_rating = ratings[0]
if n > 10:
    for i in range(0, 12):
         if ratings[i] <=  min_rating:
             min_rating = ratings[i]
         if min_stocks[i] > max_stock_of_min_rating:
             max_stock_of_min_rating = min_stocks[i]
         if ratings[i] in number_of_people_with_ratings:
             number_of_people_with_ratings[ratings[i]] += 1
         else:
             number_of_people_with_ratings[ratings[i]] = 1
    next_10_min_stock_length = 10

for i in range(n):
    to_increment = 0
    currentRateMembers = number_of_people_with_ratings[min_rating] if min_rating in number_of_people_with_ratings else 0
    if ratings[i] > min_rating and min_stocks[i] < max_stock_of_min_rating:
        to_increment = max_stock_of_min_rating - min_stocks[i] + 1
        incremented_stocks += ( next_10_min_stock_length + prev_10_min_stock_length - currentRateMembers + 1) * to_increment


    if i > 0 and i + 10 < n:
        if ratings[i + 10] in number_of_people_with_ratings:
                 number_of_people_with_ratings[ratings[i + 10]] += 1
        else:
             number_of_people_with_ratings[ratings[i]] = 1
        if min_rating > ratings[i + 10]:
            min_rating = ratings[i + 10]
            if min_stocks[i + 10] > max_stock_of_min_rating:
                max_stock_of_min_rating = min_stocks[i + 10]
    # if i > 0:
    #     if ratings[i] in number_of_people_with_ratings:
    #              number_of_people_with_ratings -= 1
    #     else:
    #          number_of_people_with_ratings[ratings[i]] = 1
    if i > 0:
        prev_10_min_stock_length += 1


    number_of_people_with_ratings[ratings[i]] -= 1