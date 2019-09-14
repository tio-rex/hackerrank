https://www.hackerrank.com/challenges/np-dot-and-cross/problem
Dot and Cross

import numpy

n = int(input())

arr_a = []
for _ in range(n):
    arr_a.append(list(map(int, input().strip().split())))

nparr_a = numpy.array(arr_a)

arr_b = []
for _ in range(n):
    arr_b.append(list(map(int, input().strip().split())))

nparr_b = numpy.array(arr_b)

print(numpy.dot(nparr_a, nparr_b))
