https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
Standardize Mobile Number Using Decorators

def format_pn(pn):
    return f'+91 {pn[-10:-5]} {pn[-5:]}'

def wrapper(f):
    def fun(l):
        l = map(format_pn, l)
        return f(l)
    return fun
  
