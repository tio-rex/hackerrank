https://www.hackerrank.com/challenges/symmetric-difference/problem
Symmetric Difference

M, A = int(input()), set(map(int, input().split()))
N, B = int(input()), set(map(int, input().split()))
print('\n'.join(map(str, sorted(list(A.symmetric_difference(B))))))
 
