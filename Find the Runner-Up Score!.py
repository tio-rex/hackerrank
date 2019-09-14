https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Find the Runner-Up Score!
    
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

print(sorted(list(set(arr))))[-2]
