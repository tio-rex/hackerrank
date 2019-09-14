https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
Regex Substitution

import re

d = {"&&" : "and","||" : "or"}
r = re.compile("(?<=\ )(" + "|".join(map(re.escape, d.keys())) + ")(?=\ )")
for _ in range(int(input())):
    print(r.sub(lambda w: d[w.string[w.start():w.end()]], input()))
    
