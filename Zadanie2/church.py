"""
    Liczebniki Churcha - Wprowadzenie:

"""

def create_church_function(f, n):
        """
            Return function f^n, that is, f applied n times - f(f(f(...f(f(x))
            For a function f^0, the church numeral is just an identity function
        """
        if n == 0:
            return lambda x : x                             # special case - f^0
        if n > 1:
            return lambda x : f(create_church_function(f, n-1)(x))
        else:
            return f


class ChurchNumeral:
    """
        Class representing a church numeral
    """
    def __init__(self, f, n):
        self.number = n
        self.base_function = f
        self.church_function = create_church_function(f, n)

    def succ(self):
        self.number += 1
        self.church_function = lambda x : self.base_function(self.church_function(x))

    def add(self, other):
        if self.base_function != other.base_function:
            return False
        else:
            self.number += other.number
            self.church_function = lambda x : self.church_function(other.church_function(x))
            return True

    def multiply(self, other):
        if self.base_function != other.base_function:
            return False
        else:
            self.number *= other.number
            self.church_function = create_church_function(self.church_function, other.number)
            return True

    def exp(self, other):
        if self.base_function != other.base_function:
            return False
        else:
            self.number = pow(self.number, other.number)
            self.church_function = create_church_function(create_church_function(self.church_function, self.number), other.number)
            return True

    def sub(self, other):
        pass

    #TODO - zlambdowac

