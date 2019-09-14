https://www.hackerrank.com/challenges/calendar-module/problem
Calendar Module

import calendar
from sys import stdin
m,d,y = map(int,stdin.readline().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
 
