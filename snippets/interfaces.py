# https://rednafi.github.io/digressions/python/2020/07/03/python-mixins.html
from abc import ABC, abstractmethod

class ICalc(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def sub(self, a, b):
        pass

# Cannot instantiate an abstract class
#i = ICalc()

class Calc(ICalc):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

c = Calc()
print(c.add(1,2))

#
#  Interface:  abstract methods only, no concrete methods and 
#              no nternal state (instance variables)
#  Abstract class:  Can contain abstract methods, concrete methods,
#              internal state
#  Mixin: Can contain abstract methods, concrete methods,
#              but no internal state


