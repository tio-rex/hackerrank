https://www.hackerrank.com/challenges/s10-basic-statistics/problem
Day 0: Mean, Median, and Mode

import numpy as np
from scipy import stats

n = int(input())
arr = list(map(int, input().split()))
print(np.mean(arr))
print(np.median(arr))
print(stats.mode(arr)[0][0])
 
