from __future__ import print_function

from church import *

THREE = succ(succ(ONE))
FOUR = succ(THREE)

def testF(x):
    return 2*x

def testG(x):
    return x + 3

def test_succ():
    print("Testing successor function:")
    for value in xrange(1,4):
        print("Expected value of f(x) = 2*x applied three times for number {}: {}".format(value, value * 2**3))
        print("Value using church numeral succ(succ(ONE)): {}".format(THREE(testF)(value)))
        print() # new line
        print("Expected value of f(x) = x + 3 applied three times for number {}: {}".format(value, value + 3*3))
        print("Value using church numeral succ(succ(ONE)): {}".format(THREE(testG)(value)))


def test_add():
    SEVEN = add(THREE, FOUR)
    for value in xrange(1,4):
        print("Expected value of f(x) = 2*x applied seven times for number {}: {}".format(value, value * 2**7))
        print("Value using church numeral add(THREE, FOUR): {}".format(SEVEN(testF)(value)))
        print() # new line
        print("Expected value of f(x) = x + 3 applied seven times for number {}: {}".format(value, value + 7*3))
        print("Value using church numeral add(THREE, FOUR)h: {}".format(SEVEN(testG)(value)))

        
        

def test_mul():
    TWELVE = mul(THREE, FOUR)
    for value in xrange(1, 4):
        print("Expected value of f(x) = 2*x applied twelve times for number {}: {}".format(value, value * 2**12))
        print("Value using church numeral mul(THREE, FOUR): {}".format(TWELVE(testF)(value)))
        print() # new line
        print("Expected value of f(x) = x + 3 applied twelve times for number {}: {}".format(value, value + 12*3))
        print("Value using church numeral mul(THREE, FOUR): {}".format(TWELVE(testG)(value)))

def test_exp():
    EIGHTY_ONE = exp(THREE, FOUR)
    for value in xrange(1, 4):
        print("Expected value of f(x) = 2*x applied eighty one times for number {}: {}".format(value, value * 2**81))
        print("Value using church numeral exp(THREE, FOUR): {}".format(EIGHTY_ONE(testF)(value)))
        print() # new line
        print("Expected value of f(x) = x + 3 applied eighty one times for number {}: {}".format(value, value + 81*3))
        print("Value using church numeral exp(THREE, FOUR): {}".format(EIGHTY_ONE(testG)(value)))        

def test_pred():
    for value in xrange(1, 4):
        print("Expected value of f(x) = 2*x applied two times for number {}: {}".format(value, value * 4))
        print("Value using church numeral pred(THREE): {}".format(pred(THREE)(testF)(value)))
        print() # new line
        print("Expected value of f(x) = x + 3 applied three times for number {}: {}".format(value, value + 9))
        print("Value using church numeral pred(FOUR): {}".format(pred(FOUR)(testG)(value)))

def test_sub():
    FIVE = sub(succ(succ(FOUR)), ONE)
    for value in xrange(1, 4):
        print("Expected value of f(x) = 2*x applied five one times for number {}: {}".format(value, value * 2 ** 5))
        print("Value using church numeral sub(SIX, ONE): {}".format(FIVE(testF)(value)))
        print() # new line
        print("Expected value of f(x) = 2*x applied two times for number {}: {}".format(value, value + 2*3))
        print("Value using church numeral sub(FIVE, THREE): {}".format(sub(FIVE, THREE)(testG)(value)))

if __name__ == '__main__':
    test_succ()
    test_add()
    test_mul()
    test_exp()
    test_pred()
    test_sub()