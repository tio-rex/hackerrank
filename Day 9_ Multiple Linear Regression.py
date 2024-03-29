https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem
Day 9: Multiple Linear Regression

from sklearn import linear_model
import numpy as np
import warnings
warnings.filterwarnings(action="ignore", module="sklearn", message="^internal gelsd")

m, n = map(int, input().split())

X = []
Y = []
for _ in range(n):
    f_y = np.array(input().split(), np.float)
    X.append(f_y[:-1])
    Y.append(f_y[-1])

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

for _ in range(int(input())):
    f = np.array(input().split(), np.float)
    y = a + np.sum(f * b)
    print(np.ceil(y * 100) / 100)
