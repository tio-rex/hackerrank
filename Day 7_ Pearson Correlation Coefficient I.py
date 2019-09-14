https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
Day 7: Pearson Correlation Coefficient I

def pearson(n, X, Y):
    mx = sum(X) / n
    my = sum(Y) / n

    sx = 0
    sy = 0
    p = 0

    for x, y in zip(X, Y):
        sx += (x - mx) ** 2
        sy += (y - my) ** 2
        p += (x - mx) * (y - my)

    sx = (sx / n) ** 0.5
    sy = (sy / n) ** 0.5

    p = p / (n * sx * sy)
    return p

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print('{:.3f}'.format(pearson(n, X, Y)))
