https://www.hackerrank.com/challenges/polar-coordinates/problem
Polar Coordinates

import math
from cmath import phase
c = complex(input())

print(math.sqrt((c.real*c.real)+(c.imag*c.imag)))
print(phase(c))
