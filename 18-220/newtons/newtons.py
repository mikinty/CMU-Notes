'''
18220 Newton's Approximation Demo

Michael You
'''
import numpy as np
import matplotlib.pyplot as plt
from math import log, exp

# CONSTANTS
CONST_IS = 1e-24
CONST_VT = 0.025
CONST_VIN = 8
CONST_R = 10

CONST_THRESHOLD = 1e-6
CONST_INIT_GUESS = 1.3

def func_iD_1 (vD, R=CONST_R, VIN=CONST_VIN, IS=CONST_IS, VT=CONST_VT):
  return IS*(exp(vD/VT) - 1)

def func_iD_2 (vD, R=CONST_R, VIN=CONST_VIN, IS=CONST_IS, VT=CONST_VT):
  return (VIN - vD)/(R)

def func_iD (vD, R=CONST_R, VIN=CONST_VIN, IS=CONST_IS, VT=CONST_VT):
  return (
    IS*(exp(vD/VT) - 1) - (VIN - vD)/(R)
  )

def func_iD_D (vD, R=CONST_R, VIN=CONST_VIN, IS=CONST_IS, VT=CONST_VT):
  return (
    (IS/VT)*exp(vD/VT) + (1/(R))
  )

def newtons(func, funcD, initGuess, THRESHOLD=CONST_THRESHOLD):
  prevVal = initGuess
  currVal = prevVal - func(prevVal)/funcD(prevVal)

  while abs(currVal - prevVal) > THRESHOLD:
    print('Iterating', currVal)
    prevVal = currVal
    currVal = prevVal - func(prevVal)/funcD(prevVal)

  return currVal  

if __name__ == "__main__":
  print('### Beginning Newton\'s Approximation ###')
  print('Init Guess, v_D =', CONST_INIT_GUESS)

  ans = newtons(func_iD, func_iD_D, CONST_INIT_GUESS)

  print('v_D converged at', ans, end='\n\n')
  print('Solution (v_D, i_D) = ({0}, {1})'.format(ans, func_iD_1(ans)), end='\n\n')

  ### PLOT CURVES AND INTERSECTION ###
  print('### PLOTTING ###')
  CONST_LINEWIDTH = 5

  vD = np.linspace(0, 1.4)
  f1 = np.vectorize(lambda vD: func_iD_1(vD))
  f2 = np.vectorize(lambda vD: func_iD_2(vD))
  iD1 = f1(vD)
  iD2 = f2(vD)

  plt.rcParams.update({'font.weight': 'bold'})
  plt.rcParams.update({'font.size': 22})

  plt.figure()
  plt.plot(vD, iD1, linewidth=CONST_LINEWIDTH)
  plt.plot(vD, iD2, linewidth=CONST_LINEWIDTH)
  plt.plot(ans, func_iD_1(ans), marker='o', markersize=15, color="red")
  plt.xlabel('$v_D$ (V)')
  plt.ylabel('$i_D$ (A)')

  plt.show()