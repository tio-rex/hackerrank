https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
Set .symmetric_difference() Operation

n = int(input())
e_set = set(map(int, input().split()))
m = int(input())
f_set = set(map(int, input().split()))
print(len(e_set.symmetric_difference(f_set)))
