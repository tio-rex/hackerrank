https://www.hackerrank.com/challenges/python-sort-sort/problem
Athlete Sort

from operator import itemgetter

n, _ = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
[print(*e) for e in sorted(arr, key=itemgetter(int(input())))]
 
