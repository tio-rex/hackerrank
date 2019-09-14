https://www.hackerrank.com/challenges/py-the-captains-room/problem
The Captain's Room

def main():
    k = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    cap = ((sum(s) * k) - sum(l)) // (k - 1)
    print(cap)

if __name__ == '__main__':
    main()
 
