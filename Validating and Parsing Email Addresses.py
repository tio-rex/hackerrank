https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
Validating and Parsing Email Addresses

import re

regex_adress = r"^[a-zA-Z0-9][a-zA-Z0-9-_.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
for _ in range(int(input())):
    name, mail = input().split()
    mail = mail[1:-1]
    if re.match(regex_adress, mail):
        print("{} <{}>".format(name, mail))
 
