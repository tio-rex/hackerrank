https://www.hackerrank.com/challenges/itertools-combinations/problem
itertools.combinations()

import itertools

char, k = input().split()
char = list(char)
char.sort()
for j in range(1, int(k) + 1):
    for i in itertools.combinations(char, j):
        print(''.join(i))
        
