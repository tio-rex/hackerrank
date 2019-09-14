https://www.hackerrank.com/challenges/saying-hi/problem
Saying Hi

n = int(input())
import re
p = re.compile('^[Hh][Ii]\s[^dD].*')
for i in range(n):
    x = str(input())
    if(len(re.findall(p, x)) > 0):
        print(x)
 
