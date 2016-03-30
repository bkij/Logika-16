#
#   test_script.py
#
#   Tests main.py/main_negated_py
#

import sys
import os
import itertools as it

def test_main():
    for item in it.product(it.combinations_with_replacement(xrange(2), 2), repeat=3):
        arg = list(it.chain(*item))
        expected = 1
        for i in arg:
            if i % 2 != 0:
                expected = 0
        arg = [str(i) for i in arg]
        print "Input: " + ' '.join(arg)
        print "Expected: " + str(expected)
        sys.stdout.write("Output: ")                # So there is no new line
        os.system("python main.py " + ' '.join(arg))
        print ""                                    # Print new line
    
def test_negated():
    for item in it.product(it.combinations_with_replacement(xrange(2), 2), repeat=3):
        arg = list(it.chain(*item))
        expected = 0
        for i in arg:
            if i % 2 != 0:
                expected = 1
        arg = [str(i) for i in arg]
        print "Input: " + ' '.join(arg)
        print "Expected: " + str(expected)
        sys.stdout.write("Output: ")                # So there is no new line
        os.system("python main_negated.py " + ' '.join(arg))
        print ""                                    # Print new line
    
if len(sys.argv) < 2:
    print "Usage: python test_script.py [main.py main_negated.py]"
    sys.exit()

if sys.argv[1] == 'main.py':
    test_main()
elif sys.argv[1] == 'main_negated.py':
    test_negated()
else:
    print "Usage: python test_script.py [main.py main_negated.py]" 

   