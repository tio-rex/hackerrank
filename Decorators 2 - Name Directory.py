https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner
    
