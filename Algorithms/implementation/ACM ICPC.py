"""
You are given a list of  people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not.
Find out the maximum number of topics a 2-person team can know. And also find out how many teams can know that maximum number of topics.

Note Suppose a, b, and c are three different people, then (a,b) and (b,c) are counted as two different teams.

Input Format

The first line contains two integers, N and M, separated by a single space, where N represents the number of people, and M represents the number of topics.  lines follow.
Each line contains a binary string of length . If the th line's th character is , then the th person knows the th topic; otherwise, he doesn't know the topic.

Constraints
2 <= N <= 500
1 <= M <= 500

Output Format

On the first line, print the maximum number of topics a 2-person team can know.
On the second line, print the number of 2-person teams that can know the maximum number of topics.

Sample Input

4 5
10101
11100
11010
00101


Sample Output

5
2


Explanation

(1, 3) and (3, 4) know all the 5 topics. So the maximal topics a 2-person team knows is 5, and only 2 teams can achieve this.
"""

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(int(topic_t, 2))
max_no_of_topics = -1
max_teams = 0
for people_i in range(n):
    people_j = people_i + 1
    while people_j < n:
        or_int = topic[people_i] | topic[people_j]    # gives the max combination of 1s
        or_no_of_topics = bin(or_int).count("1")
        if or_no_of_topics > max_no_of_topics:
            max_no_of_topics = or_no_of_topics
            max_teams = 1
        elif or_no_of_topics == max_no_of_topics:
            max_teams += 1
        people_j += 1
print(max_no_of_topics)
print(max_teams)