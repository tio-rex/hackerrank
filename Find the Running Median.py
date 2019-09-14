https://www.hackerrank.com/challenges/find-the-running-median/problem
Find the Running Median

import bisect
import sys

def find_the_running_median(num, inputs):
    medianArr = []
    for elem in inputs:
        bisect.insort(medianArr, elem)
        if len(medianArr) % 2 == 0:
            print((medianArr[int(len(medianArr)/2)] + medianArr[int(len(medianArr)/2)-1])/2)
        else:
            print(float(medianArr[int(len(medianArr)/2)]))

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for iter in range(n):
        a_i = int(input().strip())
        a.append(a_i)
    find_the_running_median(n, a)
