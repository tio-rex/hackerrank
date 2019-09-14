https://www.hackerrank.com/challenges/np-concatenate/problem
Concatenate

import numpy

n,m,p = map(int,input().split())
array_1 = []
array_2 = []
[array_1.append(list(map(int,input().split()))) for i in range(n)]
[array_2.append(list(map(int,input().split()))) for i in range(m)]
print(numpy.concatenate((array_1,array_2),axis=0))
 
