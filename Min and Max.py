https://www.hackerrank.com/challenges/np-min-and-max/problem
Min and Max

import numpy

n,m=map(int, input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
print(numpy.max(numpy.min(numpy.array(a),axis=1)))
