https://www.hackerrank.com/challenges/py-set-union/problem
Set .union() Operation

eng_num = int(input())
eng_roll_set = set(map(int,input().split()))

french_num = int(input())
french_roll_set = set(map(int,input().split()))

result_set = eng_roll_set.union(french_roll_set)
print (len(result_set))
