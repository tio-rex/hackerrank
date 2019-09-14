https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
Collections.OrderedDict()

import collections

dictionary = collections.OrderedDict()

n = int(input())
for _ in range(n):
    *item_name, net_price = input().split(' ')
    item_name = ' '.join(item_name)
    if item_name not in dictionary:
        dictionary[item_name] = int(net_price)
    else :
        dictionary[item_name] += int(net_price)

for key, value in dictionary.items():
    print(key, value)
 
