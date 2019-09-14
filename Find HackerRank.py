https://www.hackerrank.com/challenges/find-hackerrank/problem
Find HackerRank

import re

for _ in range(int(input())):
    s = input().lower()

    a = s.startswith('hackerrank')
    b = s.endswith('hackerrank')
    if a and b:
        print(0)
    elif a:
        print(1)
    elif b:
        print(2)
    else:
        print(-1)
