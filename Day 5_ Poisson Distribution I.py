https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
Day 5: Poisson Distribution I

import math
l = 2.5
k = 5
print(round(l**k*math.exp(-l)/math.factorial(k), 3))
