https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
Transpose and Flatten

import numpy

n, m = map(int, input().split())

M = numpy.array([input().split() for i in range(n)], numpy.int)

print(M.transpose())
print(M.flatten())
 
