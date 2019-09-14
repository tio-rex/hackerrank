https://www.hackerrank.com/challenges/find-angle/problem
Find Angle MBC

from math import *
ab, bc = [int(input()) for _ in range(2)]
print(str(int(degrees(atan2(ab,bc)) + 0.5))+'°')
