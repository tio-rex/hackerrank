https://www.hackerrank.com/challenges/np-linear-algebra/problem
Linear Algebra

import numpy

n,a=int(input()),[]
for i in range(n):
    a.append(list(map(float,input().split())))
print(round(numpy.linalg.det(numpy.array(a)),2))
