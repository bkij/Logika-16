#
#   test_script.py
#
#   Tests main.py/main_negated_py
#
from __future__ import print_function
import subprocess as sp
import sys
import os
import itertools as it

def my_combs(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in it.product(xrange(n), repeat=r):
        if sorted(indices) == list(indices):
             yield tuple(pool[i] for i in indices)

def test_main():
    for item in it.product(my_combs(xrange(2), 2), repeat=3):
        arg = list(it.chain(*item))
        expected = 1
        for i in arg:
            if i % 2 != 0:
                expected = 0
        arg = [str(i) for i in arg]
        call_list = ["python", "main.py"]
        call_list.extend(arg)
        out_value = sp.call(call_list)
        print("Input: " + ' '.join(arg))
        print("Expected: " + str(expected))
        print("Output: " + str(out_value))
        print("")                                    # Print new line
    
def test_negated():
    for item in it.product(my_combs(xrange(2), 2), repeat=3):
        arg = list(it.chain(*item))
        expected = 0
        for i in arg:
            if i % 2 != 0:
                expected = 1
        arg = [str(i) for i in arg]
        call_list = ["python", "main_negated.py"]
        call_list.extend(arg)
        out_value = sp.call(call_list)
        print("Input: " + ' '.join(arg))
        print("Expected: " + str(expected))
        print("Output: " + str(out_value))
        print("")                                    # Print new line
    
if len(sys.argv) < 2:
    print("Usage: python test_script.py [main.py main_negated.py]")
    sys.exit()

if sys.argv[1] == 'main.py':
    test_main()
elif sys.argv[1] == 'main_negated.py':
    test_negated()
else:
    print("Usage: python test_script.py [main.py main_negated.py]") 

   
