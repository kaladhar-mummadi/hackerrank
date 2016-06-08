hours = int(input().strip())
minutes = int(input().strip())

result = ""

words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "tweleve",
    13: "thirteen",
    14 : "fourteen",
    15:"fifteen",
    16:"sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    21 : "twenty one",
    22 : "twnety two",
    23 : "twenty three",
    24 : "twenty four",
    25 : "twenty five",
    26 : "twenty six",
    27 :"twnety seven",
    28 : "twenty eight",
    29 : "twenty nine",
}

result += words[hours]
if minutes == 0:
    result += " o' clock"
elif minutes == 1:
    result = words[minutes] + " minute past " + result
elif minutes == 15:
    result = "quarter past " + result
elif minutes < 30:
    result = words[minutes] + " minutes past " + result
elif minutes == 30:
    result = "half past " + result
elif minutes == 45:
    result = "quarter to " + words[(hours + 1) % 12]
elif minutes == 59:
    result = words[60 - minutes] + " minute to " + words[(hours + 1) % 12]
else:
    result = words[60 - minutes] + " minutes to " + words[(hours + 1) % 12]

print(result)