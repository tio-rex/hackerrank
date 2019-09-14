https://www.hackerrank.com/challenges/re-group-groups/problem
Group(), Groups() & Groupdict()

import re
result = re.search(r'([a-z0-9])\1+', input())

print(result.group(1) if result else '-1')
