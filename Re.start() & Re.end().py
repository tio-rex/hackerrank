https://www.hackerrank.com/challenges/re-start-re-end/problem
Re.start() & Re.end()

import re

s, p = input(), input()
m = [(m.start(1), m.end(1)-1) for m in re.finditer(r"(?=(%s))" % p, s)]
print(*m if m else [(-1, -1)], sep="\n")
 
