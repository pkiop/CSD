import numpy as np 
from scipy import signal

A = -4.0
B = 2.0
C = 1.0
D = 0.0
sys1 = signal.StateSpace(A,B,C,D)

