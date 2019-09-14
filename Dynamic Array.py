https://www.hackerrank.com/challenges/dynamic-array/problem
Dynamic Array

import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    list_of_seq = []
    result = []
    last_answer = 0
    for i in range(n):
        list_of_seq.append([])

    for k, x, y in queries:
        if (k == 1):
            list = list_of_seq[(x ^ last_answer) % n]
            list.append(y)
        elif (k == 2):
            list = list_of_seq[(x^last_answer) % n]
            last_answer = list[y % len(list)]
            print (last_answer)
            result.append(last_answer)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
