https://www.hackerrank.com/challenges/python-time-delta/problem
Time Delta

from datetime import datetime

def time_delta(t1, t2):
    time1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return int(abs((time1 - time2).total_seconds()))

if __name__ == '__main__':
    for _ in range(int(input())):
        print(time_delta(input(), input()))
 
