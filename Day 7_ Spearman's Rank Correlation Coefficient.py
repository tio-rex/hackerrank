https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem
Day 7: Spearman's Rank Correlation Coefficient

def spearman(n, X, Y):
    
    def rank(X):
        r = [0] * len(X)
        xs = sorted((x, i) for i, x in enumerate(X))
        for j, xi in enumerate(xs):
            r[xi[1]] = j + 1
        return r

    r = sum((rx - ry) ** 2 for rx, ry in zip(rank(X), rank(Y)))
    r = 1 - 6 * r / n / (n ** 2 - 1)

    return r

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

c = spearman(n, X, Y)
print('{:.3f}'.format(c))
