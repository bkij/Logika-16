#!/usr/bin/python
#
#   main.py
#
#   A program to check whether the first six supplied
#   command line parameters are even numbers
#

import sys

parameters = [int(i) for i in sys.argv[1:]]

if len(parameters) < 6:
    print "Usage: python main.py n1 n2 n3 n4 n5 n6"
else:
    if (parameters[0] % 2 == 0 and parameters[1] % 2 == 0 and
    parameters[2] % 2 == 0 and parameters[3] % 2 == 0 and
    parameters[4] % 2 == 0 and parameters[5] % 2 == 0):
        sys.exit(1)    # return instead of print for testing
    else:
        sys.exit(0)    # as above
