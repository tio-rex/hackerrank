https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
DefaultDict Tutorial

from collections import defaultdict

def get_index(a, b):
    d = defaultdict(list)
    for word in enumerate(a):
        d[word[1]].append(word[0] + 1)
    keys = d.keys()
    for word in b:
        if word not in keys:
            d[word].append(-1)
    return [d[word] for word in b]

def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(m)]
    for i in get_index(a, b):
        print(' '.join(map(str, i)))

if __name__ == '__main__':
    main()
