https://www.hackerrank.com/challenges/py-check-subset/problem
Check Subset

for _ in range(int(input())):
    n1 = int(input())
    set_a = set(map(int, input().split()))

    n2 = int(input())
    set_b = set(map(int, input().split()))
 
    if set_a - set_b: 
        print(False)
    else:
        print(True)
       
