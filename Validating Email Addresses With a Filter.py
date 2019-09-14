https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
Validating Email Addresses With a Filter

import re

def fun(s):
    return re.match(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s)
    
