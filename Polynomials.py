https://www.hackerrank.com/challenges/np-polynomials/problem
Polynomials

import numpy

nparray=numpy.array([float(x) for x in input().split()])
n=float(input())
print(numpy.polyval(nparray,n))
