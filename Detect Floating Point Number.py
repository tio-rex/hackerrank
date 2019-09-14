https://www.hackerrank.com/challenges/introduction-to-regex/problem
Detect Floating Point Number

if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            s = input()
            int(s)
            print("False")
        except:
            try:
                float(s)
                print("True")
            except:
                print("False")
                
