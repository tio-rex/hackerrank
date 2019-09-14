https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    line = input()

    if 'pop' == line:
        s.pop()
        continue

    command, value = line.split()
    value = int(value)

    if command == 'remove':
        s.remove(value)
    elif command == 'discard':
        s.discard(value)

print(sum(s))
