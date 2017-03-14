start_str= "min(int, "
end_str = "int)"
end_brace = ")"
n = int(input().strip())
# n - 1
number_of_start_of_functions = start_str * (n-1)
number_of_end_braces = end_brace * (n-2)
print(number_of_start_of_functions + end_str + number_of_end_braces)