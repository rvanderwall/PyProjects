
class SwordMeta(type):
    def __instancecheck__(cls, instance):
        return issubclass(type(instance), cls)


    def __subclasscheck__(cls, subclass):
        #  If the subclass has all the needed methods, it is a valid subclass
        if (
            hasattr(subclass, "swipe") and callable(subclass.swipe)
            and
            hasattr(subclass, "sharpen") and callable(subclass.sharpen)
        ):
           return True

        # OR, if the subclass is derived from super, it is a valid subclass
        return super().__subclasscheck__(subclass)


class Sword(metaclass=SwordMeta):
    """Abstract Base Class"""
    def thrust(self):
        print("Thrust!", type(self).__name__)


class BroadSword:
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
print(issubclass(Sabre, Sword), "A Sabre is oddly a subclass, even though it has none of the methods, but it does inherit")

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
print(isinstance(sa, Sword), "A sabre is an instance")

sw.thrust()
# bs.thrust()   # even though it is a subclass and instance, it has no thrust() method
# ss.thrust()   # even though it is a subclass and instance, it has no thrust() method
sa.thrust()


print()
print(BroadSword.__mro__)   # method resolution order
print(SamuraiSword.__mro__)
print(Rifle.__mro__)
print(Sabre.__mro__)
