https://www.hackerrank.com/challenges/no-idea/problem
No Idea!

_ = input()
array = input().split()
like = set(input().split())
dislike = set(input().split())
print(sum((i in like) - (i in dislike) for i in array))
