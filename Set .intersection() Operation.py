https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
Set .intersection() Operation

n = int(input())
list_a = set(map(int, input().split()))

m = int(input())
list_b = set(map(int, input().split()))

print(len(list_a.intersection(list_b)))
