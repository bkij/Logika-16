from __future__ import print_function

from church import church_numeral
import functools as ft
import random
from math import sin, cos

def linear_function_A(x):
    return 3*x + 5
    
def linear_function_B(x):
    return -34*x + 87
        
def naive_apply_n_times(f, n, x):
    """
        Evalute a string - f(f(f(...f(x)), where function f is applied n times
        Naive and a bit stupid but definitely working. For tests only
    """
    return eval((f.__name__ + "(")*n + str(x) + ")"*n)


if __name__ == '__main__':
    funcs = [sin, cos, linear_function_A, linear_function_B]
    args = xrange(1, 10)
    nums = [random.randrange(0, 15) for i in range(4)]
    # Check if church numerals work
    for f in funcs:
        for arg in args:
            for num in nums:
                print("Input function: " + f.__name__ + "^" +  str(num) + "(" + str(arg) + ") == "
                      + str(naive_apply_n_times(f, num, arg)))
                print("Church numeral of input function and degree " + str(num) + " == " 
                      + str(church_numeral(f, num)(arg)))
                print("")
