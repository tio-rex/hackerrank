https://www.hackerrank.com/challenges/py-set-mutations/problem
Set Mutations

from sys import stdin

n = int(stdin.readline())

A = set(map(int,stdin.readline().split()))

n_cmd = int(stdin.readline())

for i in range(n_cmd):
    cmd, l = stdin.readline().split()
    l = int(l)
    temp = set(map(int,stdin.readline().split()))
    if(cmd == "intersection_update"):
        A.intersection_update(temp)
    
    elif(cmd == "update"):
        A.update(temp)
    
    elif(cmd == "symmetric_difference_update"):
        A.symmetric_difference_update(temp)

    elif(cmd == "difference_update"):
        A.difference_update(temp)

print(sum(A))
