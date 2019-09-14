https://www.hackerrank.com/challenges/ginorts/problem
ginortS

s = input()
def custom_index(c):
    i = ord(c)
    if i in range(65,91):
        i += 100
    elif i in range(48,58):
        if i%2:
            i += 200
        else:
            i += 300
    return i

print(''.join(sorted(s, key=lambda c: custom_index(c))))
 
