https://www.hackerrank.com/challenges/any-or-all/problem
Any or All

n, l = int(input()), input().split()
a, b = [int(x) > 0 for x in l], [x == x[::-1] for x in l]
print(all(a) and any(b))
 
