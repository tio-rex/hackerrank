https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
itertools.combinations_with_replacement()

import itertools

char, k = input().split()
char = list(char)
char.sort()
for i in itertools.combinations_with_replacement(char, int(k)):
    print(''.join(i))
