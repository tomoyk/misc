#!/usr/bin/env python

'''
sympyで方程式を解く
'''

from sympy import *

var("x")
equation = Eq(x**3 + 2 * x**2 - 5 * x - 6, 0) # x^3+2x^2-5x-6
answer = solve(equation)
print(answer)