https://www.hackerrank.com/challenges/exceptions/problem
Exceptions

def getInt(s):
  try:
    num = int(s)
    return num, False
  except ValueError:
    print("Error Code: invalid literal for int() with base 10: '%s'" % (s))
    return 0, True
  except:
    print("Something else went wrong")
    return 0, True

T = int(input())
for idx in range(T):
  nums = list(map(str, input().split()))

  dividend, error = getInt(nums[0])
  if (error):
    continue

  divisor, error = getInt(nums[1])
  if (error):
    continue

  try:
    print(int(dividend/divisor))
  except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")
  except:
    print("Something else went wrong")
    
