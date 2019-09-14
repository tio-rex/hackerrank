https://www.hackerrank.com/challenges/np-eye-and-identity/problem
Eye and Identity

import numpy as np

np.set_printoptions(sign=' ')
m, n = map(int, input().split(' '))
print(np.eye(m, n))
