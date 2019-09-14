https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
Day 4: Geometric Distribution II

ans = 0
p = 1 / 3
for i in range(1, 6):
    ans += (1-p)**(i-1) * p
print(round(ans, 3))
