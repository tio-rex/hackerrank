https://www.hackerrank.com/challenges/string-validators/problem
String Validators

if __name__ == "__main__":

    string = input().strip()

    digit = False
    lower = False
    upper = False

    for char in string:

        if( not digit ): digit = char.isdigit()
        
        if( not lower ): lower = char.islower()
        
        if( not upper ): upper = char.isupper()

        if( digit and lower and upper ): break

    print( ( lower or upper or digit ) )

    print( ( lower or upper ) )

    print( digit )

    print( lower )

    print( upper )
 
