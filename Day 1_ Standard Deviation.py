https://www.hackerrank.com/challenges/s10-standard-deviation/problem
Day 1: Standard Deviation

n = int(input())
arr = list(map(int, input().split()))
avg = sum(arr) / len(arr)
std = (sum([(arr[x] - avg)**2 for x in range(n)])/n)**(1/2)
print(std)
 
