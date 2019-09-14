https://www.hackerrank.com/challenges/designer-door-mat/problem
Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT

def designer_door_mat(n, m):
    for i in range(1, n, 2):
        print(str('.|.' * i).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in range(n-2, -1, -2):
        print(str('.|.' * i).center(m, '-'))

if __name__ == '__main__':
    N, M = map(int, input().split())
    designer_door_mat(N, M)
