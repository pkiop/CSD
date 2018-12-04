from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x1 = Symbol('x1')
x2 = Symbol('x2')
t = Symbol('t')

F = 10000000

x1dot = Derivative(x1,t)
x2dot = Derivative(x2,t)
x1dot2 = Derivative(x1dot,t)
x2dot2 = Derivative(x2dot,t)

m1 = 17*1000
m2 = 754.2*1000
k = 1252*1000
u = 0.02
g = 9.8


F1 = F - k * (x1 - x2) - u * m1 * g * x1dot
x1dot2 = F1 / m1
x1dot = Integral(x1dot2, t)
x1 = Integral(x1dot, t)

F2 = k*(x1 - x2) - u*m2*g*x2dot

x2dot2 = F2 / m2
x2dot = Integral(x2dot2, t)
x2 = Integral(x2dot, t)

t = Float(1)
plt.plot(t, x1dot)
