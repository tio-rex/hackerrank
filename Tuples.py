https://www.hackerrank.com/challenges/python-tuples/problem
Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    l= tuple(integer_list)
    print (hash(l))
 
