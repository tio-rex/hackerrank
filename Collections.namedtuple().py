https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
Collections.namedtuple()

from collections import namedtuple
import collections
from string import ascii_uppercase

grade = 0
num = int(input())

for i in range(1):
    word = input().split()
Student = collections.namedtuple('Student',word) 

for i in range(num):
    info = input().split()
    S = Student(info[0],info[1],info[2],info[3])
    grade = int((S.MARKS)) + grade

avg = round(grade/num,3)
print(avg)
 
