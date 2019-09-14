https://www.hackerrank.com/challenges/collections-counter/problem
collections.Counter()

import collections

nS = int(input())
s = collections.Counter(map(int, input().split()))
nC = int(input())
a = 0
for i in range(nC):
    size, p = map(int, input().split())
    if s[size]:
        a += p
        s[size] -= 1
print (a)
 
