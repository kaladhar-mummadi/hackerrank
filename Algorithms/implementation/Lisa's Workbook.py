no_of_chapters, max_no_problems_per_chapter = [int(a_temp) for a_temp in input().strip().split(' ')]
number_of_problems_for_each_chapter = [int(a_temp) for a_temp in input().strip().split(' ')]
total_no_of_pages = 0
special_problems = 0
for i in range(no_of_chapters):
    no_of_pages_for_each_chapter = int(number_of_problems_for_each_chapter[i]/max_no_problems_per_chapter) + \
                                   (0 if number_of_problems_for_each_chapter[i]%max_no_problems_per_chapter == 0 else 1)
    problem_numbers = 0
    for j in range(no_of_pages_for_each_chapter):
        start_prob = problem_numbers + 1
        end_prob = max_no_problems_per_chapter * (j + 1)
        end_prob = end_prob if end_prob <= number_of_problems_for_each_chapter[i] else number_of_problems_for_each_chapter[i]
        current_page = total_no_of_pages + j + 1
        if current_page >= start_prob and current_page <= end_prob:
            special_problems += 1
        problem_numbers = end_prob
    total_no_of_pages += no_of_pages_for_each_chapter
print(special_problems)