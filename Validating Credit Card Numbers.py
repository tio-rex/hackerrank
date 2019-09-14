https://www.hackerrank.com/challenges/validating-credit-card-number/problem
Validating Credit Card Numbers

import sys
import re

def debug (msg):
    print(msg, file=sys.stderr)
    return

n = int(input())
r1 = re.compile(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$')
r2 = re.compile(r'.*([0-9])\1{3,}')
for _ in range(n):
    line = input()
    check = "Invalid"
    if r1.match(line) and not r2.match(line.replace("-","")):
        check = "Valid"
    print(check)
 
