https://www.hackerrank.com/challenges/itertools-permutations/problem
itertools.permutations()

from itertools import permutations

s = input().split(" ")

print(*[''.join(i) for i in permutations(sorted(s[0]),int(s[1]))], sep = "\n")
