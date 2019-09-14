https://www.hackerrank.com/challenges/np-sum-and-prod/problem
Sum and Prod

import numpy

n, m = map(int, input().split())
A = numpy.array([input().split() for i in range(n)], numpy.int)

print(numpy.prod(numpy.sum(A, axis=0)))
 
