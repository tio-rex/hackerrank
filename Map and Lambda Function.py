https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
Map and Lambda Function

cube = lambda x: x**3
# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a,b = [0, 1]
    for i in range(n):
        yield a
        a, b = b, a + b
