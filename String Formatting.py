https://www.hackerrank.com/challenges/python-string-formatting/problem
String Formatting

def print_formatted(number):
    padding = len('{:b}'.format(number))

    for i in range(1, number + 1):
        decimal = '{:d}'.format(i).rjust(padding)
        octal = '{:o}'.format(i).rjust(padding)
        hexa = '{:x}'.format(i).rjust(padding).upper()
        binary = '{:b}'.format(i).rjust(padding)

        print(' '.join([decimal, octal, hexa, binary]))
       
