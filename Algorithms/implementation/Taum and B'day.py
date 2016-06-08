"""
Taum is planning to celebrate the birthday of his friend, Diksha.
There are two types of gifts that Diksha wants from Taum: one is black and the other is white.
To make her happy, Taum has to buy  number of black gifts and number of white gifts.

The cost of each black gift is  units.
The cost of every white gift is  units.
The cost of converting each black gift into white gift or vice versa is  units.
Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

Input Format

The first line will contain an integer  which will be the number of test cases.
There will be  pairs of lines. The first line of each test case will contain the values of integers  and .
Another line of each test case will contain the values of integers , , and .

Constraints


Output Format

 lines, each containing an integer: the minimum amount of units Taum needs to spend on gifts.


"""
no_of_test_cases = int(input().strip())
for _ in range(no_of_test_cases):
    black, white = input().strip().split(' ')
    black, white = [int(black), int(white)]
    cost_of_black, cost_of_white, exchange_cost = [int(temp) for temp in input().strip().split(' ')]

    # if other color's actual cost + exchange cost is less than present color, then make it two step process fo current color
    two_step_cost_for_black = (cost_of_white + exchange_cost)
    if two_step_cost_for_black < cost_of_black:
        cost_of_black = two_step_cost_for_black
    else:
        two_step_cost_for_white = (cost_of_black + exchange_cost)
        if  two_step_cost_for_white < cost_of_white:
            cost_of_white = two_step_cost_for_white

    # cost_of_black = (cost_of_white + exchange_cost) if (cost_of_white + exchange_cost) < cost_of_black else cost_of_black
    # cost_of_white = (cost_of_black + exchange_cost) if (cost_of_black + exchange_cost) < cost_of_white else cost_of_white

    result = black * cost_of_black + white * cost_of_white
    print(result)