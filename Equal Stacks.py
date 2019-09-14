https://www.hackerrank.com/challenges/equal-stacks/problem
Equal Stacks

import os
import sys
import math

def equalStacks(h1, h2, h3):
    sh1 = sum(h1)
    sh2 = sum(h2)
    sh3 = sum(h3)

    while h1 and h2 and h3:
        if sh1 == sh2 == sh3:
            return sh1
        elif sh1 >= max(sh2,sh3):
            sh1 -= h1.pop(0)
        elif sh2 >= max(sh1,sh3):
            sh2 -= h2.pop(0)
        else:
            sh3 -= h3.pop(0)

    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
