https://www.hackerrank.com/challenges/zipped/problem
Zipped!

student, tests = map(int, input().split())
int_list = []
for _ in range(tests):
    int_list += [list(map(float, input().split()))]
  
for a in zip(*int_list):
    print(sum(a) / tests)
 
