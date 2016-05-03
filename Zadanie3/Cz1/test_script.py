#!/usr/bin/python
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

def combinations01(n):
    if n == 1:
        for i in ['0','1']:
            yield i
    else:
        for i in ['0','1']:
            for j in combinations01(n-1):
                yield [i] + [elem for elem in it.islice(j, None)]

def test_main():
    for item in combinations01(6):
        expected = 1
        for i in item:
            if int(i) % 2 != 0:
                expected = 0
        call_list = ["python", "main.py"]
        call_list.extend(item)
        out_value = sp.call(call_list)
        print("Input: " + ' '.join(item))
        print("Expected: " + str(expected))
        print("Output: " + str(out_value))
        print("")                                    # Print new line
    
def test_negated():
    for item in combinations01(6):
        expected = 0
        for i in item:
            if int(i) % 2 != 0:
                expected = 1
        call_list = ["python", "main_negated.py"]
        call_list.extend(item)
        out_value = sp.call(call_list)
        print("Input: " + ' '.join(item))
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

   
