https://www.hackerrank.com/challenges/python-lists/problem
Lists

if __name__ == '__main__':
    arg1 = input()
    l = []
    for _ in range(int(arg1)):
        s = input().split()
        if (s[0] != 'print'):
            eval("l.{}(".format(s[0])+','.join(s[1:])+")")
        else:
            print(l)
