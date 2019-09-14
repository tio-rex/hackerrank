https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
Re.findall() & Re.finditer()

import re

v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), re.I)
print('\n'.join(m or ['-1']))
  
