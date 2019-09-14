https://www.hackerrank.com/challenges/py-set-add/problem
Set .add()

def count_unique():
    N = int(input())
    i = 0
    SET = set()
    
    try: 
        while (i < N ):
            country = input()
            SET.add(country)
            i =+ 1
    except: 
        EOFError
    length = len(SET)
    print(length)
if __name__ == "__main__":
    count_unique()
