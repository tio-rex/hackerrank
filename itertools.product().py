https://www.hackerrank.com/challenges/itertools-product/problem
itertools.product()

from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))
res = list(product(A,B))
print(*(res))
 
