https://www.hackerrank.com/challenges/arrays-ds/problem
Arrays - DS

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(arr):
    result = arr[::-1]
    return result
arrСount = int(input())
arr = list(map(int, input().rstrip().split()))
result = reverseArray(arr)
print(*result)
 
