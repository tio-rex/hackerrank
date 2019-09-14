https://www.hackerrank.com/challenges/capitalize/problem
Capitalize!

def solve(s):
    s=s.split(" ")
    x=''
    for i in s:
        x=x+i.capitalize()+" "
    return x
   
