s1 = input()
s2 = input()

m = len(s1)

# prev_lcs = [0]* (m + 1)
# cur_lcs = [0]* (m + 1)
# i = 0
# while i < m + 1:
#     j = 0
#     while j < m + 1:
#         if s1[i - 1] == s2[j - 1]:
#             cur_lcs[j] = 1 + prev_lcs[j-1]
#         else:
#             cur_lcs[j] = max(prev_lcs[j], cur_lcs[j-1])
#         j += 1
#     i += 1
prev_lcs = [0] * (len(s2) + 1)
curr_lcs = [0] * (len(s2) + 1)
for c1 in s1:
    curr_lcs, prev_lcs = prev_lcs, curr_lcs
    for j, c2 in enumerate(s2, 1):
        curr_lcs[j] = (
            1 + prev_lcs[j - 1] if c1 == c2 else
            max(prev_lcs[j], curr_lcs[j - 1])
        )
print(curr_lcs[-1])