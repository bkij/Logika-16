#coding=UTF-8
"""
    Church numerals
    B. Kijanka
"""

ZERO = lambda f : lambda x : x
ONE = lambda f : lambda x : f(x)
ZERO_PAIR = (ZERO, ZERO)

def succ(church_numeral):
    """
        Successor function for a church numeral as defined by lambda calculus:

            λabc.b(abc)
        
        When given a church numeral λfx.f(f(f...(x))), where f is applied n times,
        it simplifies to λbc.b(b^n(c)), which computes the function
        taken to the power n + 1 - the successive church numeral
    """
    return lambda f : lambda x : f(church_numeral(f)(x))

def add(church_numeral_first, church_numeral_second):
    """
        Function adding two church numerals as defined by lambda calculus:
        Applying the succesor function church_numeral_first times to the second numeral
    """
    return lambda f : lambda x: church_numeral_first(succ)(church_numeral_second)(f)(x)

def mul(church_numeral_first, church_numeral_second):
    """
        Function multiplying two church numerals as defined by lambda calculus:

            λabc.a(bc)

        When given a church numeral λfx.f(f(f...(x))), where f is applied n times
        and a church numeral λfx.f(f(f(f...(x)))), where f is applied m times,
        it simplifies to λc.λfc.f^m(f^m...(c)) -> λfc.f^m(f^m...(c)), where f^m is applied n times,
        which equals the church numeral m*n
    """
    return lambda f : lambda x : church_numeral_first(church_numeral_second(f))(x)

def exp(church_numeral_first, church_numeral_second):
    """
        Function exponentiating first church numeral to the power of church_numeral_second

        Using identity: x^y = 1*x*x*...*x (multiplying one by x y times)
    """
    return lambda f : lambda x : church_numeral_second(mul(ONE, church_numeral_first))(f)(x)

def pair_successor(church_pair):
    """
        Function creating a church numeral pair (n+1, n) from a (n, n-1) pair, or in base case
        (0,0) -> (1,0)

        Used for the predecessor function and ultimately for substracting church numerals
    """
    return (lambda f : lambda x : f(church_pair[0](f)(x)), lambda f : lambda x : church_pair[0](f)(x))

def pred(church_numeral):
    """
        Predecessor function for a church numeral

        Works by calculating church numeral pairs of the form (n, n-1) using a successor
        function, up to the pair (church_numeral, church_numeral - 1)
        and returning the second element of the pair
    """
    return lambda f : lambda x : church_numeral(pair_successor)(ZERO_PAIR)[1](f)(x)

def sub(church_numeral_first, church_numeral_second):
    """
        Function substracting the second church numeral from the first by
        applying the predecessor function church_numeral_second times to church_numeral_first

        If church_numeral_second > church_numeral_first it returns a 0 church numeral (as we encode
        only natural numbers)
    """
    return lambda f : lambda x : church_numeral_second(pred)(church_numeral_first)(f)(x)