https://www.hackerrank.com/challenges/array-left-rotation/problem
Left Rotation

def array_left_rotation(a, n, k):
    k = k % n
    return a[k:] + a[:k]

n, k = map(int, input().split())
a = list(map(int, input().split()))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
