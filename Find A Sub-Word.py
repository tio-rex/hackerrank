https://www.hackerrank.com/challenges/find-substring/problem
Find A Sub-Word

import re

s = " ".join(input() for _ in range(int(input())))

for _ in range(int(input())):
    sw = input()
    print(len(re.findall(r"\b[\d\w]+" + sw + r"[\d\w]+\b", s)))
