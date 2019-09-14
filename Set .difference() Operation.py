https://www.hackerrank.com/challenges/py-set-difference-operation/problem
Set .difference() Operation

n = int(input())
e_set = set(map(int, input().split()))

m = int(input())
f_set = set(map(int, input().split()))

print(len(e_set.difference(f_set)))
