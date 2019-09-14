https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
Introduction to Sets

def average(array):
    # your code goes here
    a = sum(set(array))
    b = len(set(array))
    return a / b
