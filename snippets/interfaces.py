# https://rednafi.github.io/digressions/python/2020/07/03/python-mixins.html
from abc import ABCMeta
from abc import ABC, abstractmethod

class ICalc(ABC):
    @abstractmethod
    def add(self, a, b):
        raise NotImplementedError

    @abstractmethod
    def sub(self, a, b):
        raise NotImplementedError

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

class Sword_from_meta(metaclass=ABCMeta):
    """Abstract Base Class"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            (
                hasattr(subclass, "swipe") and callable(subclass.swipe)
                and
                hasattr(subclass, "sharpen") and callable(subclass.sharpen)
            )
            or
            NotImplemented      # Fall back on registration mechanism
        )

    def thrust(self):
        print("Thrust!", type(self).__name__)


class Sword(ABC):
    """Abstract Base Class"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            (
                hasattr(subclass, "swipe") and callable(subclass.swipe)
                and
                hasattr(subclass, "sharpen") and callable(subclass.sharpen)
            )
            or
            NotImplemented      # Fall back on registration mechanism
        )

    def thrust(self):
        print("Thrust!", type(self).__name__)


## Not desirable, since it makes unclear what it means to be a sword
@Sword.register
class LightSabre:
    def swipe(self):
        print("fffkrrshwoooom.", type(self).__name__)

    ## There is no sharpen method, but we still want this to be a subclass.
    

class BroadSword(Sword):
    def swipe():
        print("Slash", type(self).__name__)

    def sharpen():
        print("Shink", type(self).__name__)


class SamuraiSword:
    def swipe():
        print("Slice", type(self).__name__)

    def sharpen():
        print("Shink", type(self).__name__)


class Rifle:
    def fire(self):
        print("Bang")


class Sabre(Sword):
    pass


print(issubclass(BroadSword, Sword), "A Broadsword is certainly a subclass")
print(issubclass(SamuraiSword, Sword), "A SamuraiSword is certainly a subclass")
print(issubclass(Rifle, Sword), "A Rifle is certainly NOT a subclass")
print(issubclass(Sabre, Sword), "A Sabre is NOT a subclass, it has none of the methods, even though it does inherit")
print(issubclass(LightSabre, Sword), "A lightSabre is a subclass, even though it doesn't have all the methods")

print()

sw = Sword()
bs = BroadSword()
ss = SamuraiSword()
rf = Rifle()
sa = Sabre()
print(isinstance(sw, Sword), "A sword is an instance (abstract, but still instantiated)")
print(isinstance(bs, Sword), "A broadsword is an instance")
print(isinstance(ss, Sword), "A samuria is an instance")
print(isinstance(rf, Sword), "A rifle is NOT an instance")
print(isinstance(sa, Sword), "A sabre is NOT an instance")

sw.thrust()
# bs.thrust()   # even though it is a subclass and instance, it has no thrust() method
# ss.thrust()   # even though it is a subclass and instance, it has no thrust() method
sa.thrust()


print()
print(BroadSword.__mro__)   # method resolution order
print(SamuraiSword.__mro__)
print(Rifle.__mro__)
print(Sabre.__mro__)
