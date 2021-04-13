
import string


greet = string.Template("Hello, $name.  this is $greeter")

g = greet.substitute(name="Rob", greeter="Mac")
print(g)


from collections import namedtuple
Point = namedtuple('Point', 'x y z')
p = Point(3.0, 4.0, 5.0)
print(p.z)



class C:
    def __getattr__(self, name):
        print(f"Asked for attribute {name}")
        return 5
c = C()
print(f'c.foo={c.foo}')

class Mock:
    def __init__(self):
        self.calls = []

    def __getattr__(self, name):
        def fake_method(*args):
            print(f"called mock method {name}")
            self.calls.append((name, args))
        return fake_method

m = Mock()
m.open("file_to_open")
m.close()

